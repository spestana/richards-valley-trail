from glob import glob
import re

image_list = glob('images/*.jpg')
image_list = ['../' + x.replace('\\', '/') for x in image_list]

this_i = 0
for i, image in enumerate(image_list):
    i+=1
    
    if i % 2 == 1:
        a_or_b = 'a'
        a_or_b_opposite = 'b'
        this_i += 1
        i_next = this_i+1
    
    if i % 2 == 0:
        a_or_b = 'b'
        a_or_b_opposite = 'a'
        this_i = this_i
        i_next = this_i-1
        
    print('image, ',i, ' is a(n) ', a_or_b, ' image.', this_i, i_next)
    
    html_text = f'<html> \
                    <head> \
                        <link rel="stylesheet" type="text/css" href="style.css"> \
                    </head> \
                    <body> \
                        <table width="100%"> \
                            <tr> \
                                <td></td> \
                                <td></td> \
                                <td></td> \
                            </tr> \
                            <tr> \
                                <td></td> \
                                <td width="90%"><a href="{i_next}{a_or_b}.html"><img src="{image}" width="90%"/></a></td> \
                                <td></td> \
                            </tr> \
                            <tr> \
                                <td></td> \
                                <td><em>Click image to move forward. <a href="{this_i}{a_or_b_opposite}.html">Click here to turn around.</a></em> \
                                    <p></p></td> \
                                <td></td> \
                            </tr> \
                        </table> \
                    </body> \
                <html>'
    
    
    with open(f'./pages/{this_i}{a_or_b}.html', 'w') as f:
            f.write(html_text)