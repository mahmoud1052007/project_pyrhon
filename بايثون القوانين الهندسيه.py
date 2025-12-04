import math
print('-------- Welcome to the account of the laws of some geometric shapes --------\n')
shape =input('choose the geometrip shape:(triangle, square, rectangle, parallelogram, circle, cube, cone, cylinder, sphere, cuboid,pyramid) :')

if shape =='triangle' :
    L_T =input('choose the low,choose the theory :')
    if L_T=='low' :
        type_=input('perimeter,area:')
        if type_=='perimeter':
            num1=float(input('side a:'))
            num2=float(input('side b:'))
            num3=float(input('side c:'))
            total=num1+num2+num3
            print(round(total,2))
        elif type_=="area":
            base=float(input('base a:'))
            heigh=float(input('heigh b:'))
            total=0.5*heigh*base
            print(round(total,2))
        else:
            print('Re-select the law')
    if L_T=='theory':
        print('pythagoras')
        name_rib=input('Calculating the length (hypotenuse, base, height) of a right triangle:')
        if name_rib=='hypotenuse':
            a=float(input('base:'))
            b=float(input('height:'))
            c=math.sqrt(a*2+b*2)
            print(round(c,2))
        elif name_rib=='base':
            b=float(input('height:'))
            c=float(input('hypotenuse:'))
            a=math.sqrt(c*2-b*2)
            print(round(a,2))
        elif name_rib=='height':
            c=float(input('hypotenuse:'))
            a=float(input('base:'))
            b=math.sqrt(c*2-a*2)
            print(round(b,2))
        else:
            print('Re-select the theory')

elif shape =='square':
    lows=input('choose:(perimeter,area,diameter):')
    if lows=='perimeter':
        side =float(input('length of side of square :'))
        result=side*4
        print(round(result,2))
    elif lows=='area':
        side =float(input('length of side of square :'))
        result=side**2
        print(round(result,2))
    
    elif lows=='diameter':
        side =float(input('length of side of square :'))
        result=side* math.sqrt(2)
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape=='rectangle':
    lows=input('choose:(perimeter,area,diameter):')
    if lows=='perimeter':
        l =float(input('enter the lentgth of the rectangle :'))
        w=float(input('enter the rectangle width :'))
        result=(l+w)*2
        print(round(result,2))
    elif lows=='area':
        l =float(input('enter the lentgth of the rectangle :'))
        w=float(input('enter the rectangle width :'))
        result=l*w
        print(round(result,2))
    elif lows=='diameter':
        l =float(input('enter the lentgth of the rectangle :'))
        w=float(input('enter the rectangle width :'))
        result=math.sqrt(l*2 +w*2)
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='parallelogram':
    lows=input('choose:(perimeter,area):')
    if lows=='perimeter':
        side1 =float(input('length of side of parallelogram :'))
        side2 =float(input('length of side of parallelogram :'))
        result=(side1+side2)*2
        print(round(result,2))
    elif lows=='area':
        b =float(input('length of base of parallelogram :'))
        h =float(input('length of height of parallelogram :'))
        result=b*h
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='circle':
    lows=input('choose:(perimeter,area) :')
    if lows=='perimeter':
        r=float(input('enter the radius of the circle :'))
        result=2*(math.pi)*r
        print(round(result,2))
    elif lows=='area':
        r=float(input('enter the radius of the circle :'))
        result=math.pi * r ** 2
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='cube':
    lows=input('choose:(lateral area,total area,volume,diameter) :')
    if lows=='lateral area':
        a=float(input('Enter the length of the side of the cube :'))
        result=4* a**2
        print(round(result,2))
    elif lows=='total area':
        a=float(input('Enter the length of the side of the cube :'))
        result=6* a**2
        print(round(result,2))
    elif lows=='volume':
        a=float(input('Enter the length of the side of the cube :'))
        result=a**3
        print(round(result,2))
    elif lows=='diameter':
        a=float(input('Enter the length of the side of the cube :'))
        result=a* math.sqrt(3)
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='cuboid':
    lows=input('choose:(lateral area,total area,volume,diameter) :')
    if lows=='lateral area':
        l= float(input('enter the lentgth of the cuboid :'))
        w=float(input('enter the cuboid width :'))
        h=float(input('enter the height of the cuboid :'))
        result=2*h*(l+w)
        print(round(result,2))
    elif lows=='total area':
        l= float(input('enter the lentgth of the cuboid :'))
        w=float(input('enter the cuboid width :'))
        h=float(input('enter the height of the cuboid :'))
        result=2*(l*w + l*h + w*h)
        print(round(result,2))
    elif lows=='volume':
        l= float(input('enter the lentgth of the cuboid :'))
        w=float(input('enter the cuboid width :'))
        h=float(input('enter the height of the cuboid :'))
        result=l*h*w
        print(round(result,2))
    elif lows=='diameter' :
        l= float(input('enter the lentgth of the cuboid :'))
        w=float(input('enter the cuboid width :'))
        h=float(input('enter the height of the cuboid :'))
        result=math.sqrt(l*2 + w2 + h*2)
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='cylinder':
    lows=input('choose:(lateral area,total area,volume) :')
    if lows=='lateral area':
        h=float(input('enter the height of the cylinder :'))
        r=float(input('enter the radius of the cylinder :'))
        result=2*h*r*math.pi
        print(round(result,2))
    elif lows=='total area':
        h=float(input('enter the height of the cylinder :'))
        r=float(input('enter the radius of the cylinder :'))
        result=2*r*(r+h)*math.pi
        print(round(result,2))
    elif lows=='volume':
        h=float(input('enter the height of the cylinder :'))
        r=float(input('enter the radius of the cylinder :'))
        result=math.pi*h* r**2
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='cone':
    lows=input('choose:(lateral area,total area,volume) :')
    if lows=='lateral area':
        l=float(input('Enter the length of the cone is radius :'))
        r=float(input('enter the radius of the cone :'))
        result=r*l*math.pi
        print(round(result,2))
    elif lows=='total area':
        l=float(input('Enter the length of the cone is radius :'))
        r=float(input('enter the radius of the cone :'))
        result=r*(r+l)*math.pi
        print(round(result,2))
    elif lows=='volume':
        h=float(input('enter the height of the cone :'))
        r=float(input('enter the radius of the cone :'))
        result=1/3* r**2 *h*math.pi
        print(round(result,2))
    else:
        print('Re-select the law')

elif shape =='sphere':
    lows=input('choose:(total area,volume) :')
    if lows=='total area':
        r=float(input('enter the radius of the sphere :'))
        result=4*math.pi*r**2
        print(round(result,2))
    elif lows=='volume':
        r=float(input('enter the radius of the sphere :'))
        result=4/3* r**3 *math.pi
        print(round(result,2))
    else:
        print('Re-select the law')
elif shape =='pyramid':
    
    lows=input('choose:(lateral area,total area,volume) :')
    if lows=='lateral area':
        base_perimeter=float(input('Enter the base perimeter :'))
        l=float(input('Enter the italic hength :'))
        result=base_perimeter*0.5*l
        print(round(result,2))
    elif lows=='total area':
        base_area=float(input('Enter the base area :'))
        lateral_area=float(input('Enter the lateral area :'))
        result=base_area+lateral_area
        print(round(result,2))
    elif lows=='volume':
        base_area=float(input('Enter the base area :'))
        h=float(input('Enter the height :'))
        result=base_area*h* 1/3
        print(round(result,2))
    else:
        print('Re-select the law')

else:
    print('Error in writing the geometric shape or the geometric shape does not exist. Re-enter the geometric shape again')

print('-------- GOOD BAY --------')