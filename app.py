import streamlit as st

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

st.title('Shape Calculator')

shape = st.selectbox('Choose a shape:', ['Rectangle', 'Square'])

if shape == 'Rectangle':
    width = st.number_input('Width:', min_value=0.0)
    height = st.number_input('Height:', min_value=0.0)
    rectangle = Rectangle(width, height)
    st.write(f'Rectangle Area: {rectangle.area()}')
    st.write(f'Rectangle Perimeter: {rectangle.perimeter()}')

elif shape == 'Square':
    side = st.number_input('Side Length:', min_value=0.0)
    square = Square(side)
    st.write(f'Square Area: {square.area()}')
    st.write(f'Square Perimeter: {square.perimeter()}')
