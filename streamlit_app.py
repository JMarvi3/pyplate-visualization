import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from pyplate import Substance, Container, Plate, Recipe
import time

water = Substance.liquid(name='H2O', mol_weight=18.01528, density=1.0)
water_stock = Container(name='water stock', initial_contents=[(water, '1 L')])
plate1 = Plate('plate1', max_volume_per_well='60 uL')
plate2 = Plate('plate2', max_volume_per_well='60 uL')

recipe = Recipe()
recipe.uses(water_stock, plate1, plate2)

recipe.transfer(source=water_stock, destination=plate1, quantity='10 uL')
recipe.transfer(source=plate1, destination=plate2, quantity='3 uL')
recipe.transfer(source=plate1['C:3'], destination=plate2['A:1'], quantity='1 uL')
recipe.bake()

steps = recipe.steps

st.code("""
water = Substance.liquid(name='H2O', mol_weight=18.01528, density=1.0)
water_stock = Container(name='water stock', initial_contents=[(water, '1 L')])
plate1 = Plate('plate1', max_volume_per_well='60 uL')
plate2 = Plate('plate2', max_volume_per_well='60 uL')

recipe = Recipe()
recipe.uses(water_stock, plate1, plate2)

recipe.transfer(source=water_stock, destination=plate1, quantity='10 uL')
recipe.transfer(source=plate1, destination=plate2, quantity='3 uL')
recipe.transfer(source=plate1['C:3'], destination=plate2['A:1'], quantity='1 uL')
recipe.bake()""")
index = st.slider('step', 1, len(steps))
placeholder = st.empty()

st.html(steps[index-1]._repr_html_())

