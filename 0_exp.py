import os

psnr_list = []
ssim_list = []

for coef in range(0, 65):
    msg = os.popen(f'python main.py --input input.jpg --coeffs {coef}')
    output = msg.read()
    print(output, end='')

    
