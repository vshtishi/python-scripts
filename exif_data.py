from PIL import Image
import piexif
import os
import aux_data

path = '/home/user/watermarked_images'
result = '/home/user/watermarked_exif'
directory = os.fsencode(path)


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)

    im = Image.open(path + '/' + filename)
    exif_dict = piexif.load(im.info["exif"])

    state = filename.rsplit('-', 1)[1]
    article_type = filename.rsplit('-', 1)[0]
    state_slug = state.replace('.jpg', '')
    state = state_slug.capitalize()
    owner = state + '.domain.org'
    print(article_type)

    exif_dict["0th"][piexif.ImageIFD.Copyright] = owner
    exif_dict["Exif"][piexif.ExifIFD.CameraOwnerName] = owner

    if '[state_name]' not in aux_data.headings[article_type]:
        exif_dict["0th"][piexif.ImageIFD.ImageDescription] = aux_data.headings[article_type] + ' ' + aux_data.state_names[state_slug]
    else:
        header = aux_data.headings[article_type]
        header = header.replace('[state_name]', aux_data.state_names[state_slug])
        exif_dict["0th"][piexif.ImageIFD.ImageDescription] = header

    exif_bytes = piexif.dump(exif_dict)

    im.save(result + '/' + filename, "jpeg", exif=exif_bytes)
