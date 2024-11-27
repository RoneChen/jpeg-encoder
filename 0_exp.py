import os


def coefficient_analysis():
    r'''
    This function is used to analyze the coefficients of the DCT (Discrete Cosine Transform) in an image.
    '''
    for coef in range(0, 65):
        msg = os.popen(f'python main.py --input input.jpg --coeffs {coef}')
        output = msg.read()
        print(output, end='')

def scale_factor_analysis():
    r'''
    This function is used to analyze the impact of the scale factor on the quality of the reconstructed image.
    '''
    for scale_factor in [1, 2, 4, 8, 16, 32]:
        msg = os.popen(f'python main.py --input input.jpg --scale-factor {scale_factor}')
        output = msg.read()
        print(output, end='')

if __name__ == "__main__":
    scale_factor_analysis()
        
