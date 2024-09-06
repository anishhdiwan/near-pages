# from rembg import remove
# from PIL import Image

# input_path = "/home/anishdiwan/temp_stop_motion/frame_10.png"
# output_path = "output.png"

# with open(input_path, "rb") as input_file:
#     input_data = input_file.read()
#     output_data = remove(input_data)

# with open(output_path, "wb") as output_file:
#     output_file.write(output_data)


from pathlib import Path
from rembg import remove, new_session

model_name = "isnet-general-use"
session = new_session(model_name)

for file in Path('./images/stills/walk').glob('*.png'):
    input_path = str(file)
    output_path = str(file.parent / (file.stem + ".out.png"))

    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input, session=session, bgcolor=(255, 255, 255, 0), alpha_matting=True, alpha_matting_foreground_threshold=270,alpha_matting_background_threshold=200, alpha_matting_erode_size=11)
            o.write(output)