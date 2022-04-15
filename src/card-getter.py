import os
import sys
import requests
import json
import wget
import scrython

class CardGetter():
    #def __init__(self, api_key):
    def __init__(self):
        self.api_key = api_key

    def get_the_cards(card_list):
        for card_name in card_list:
            # 1. get clean card pngs from scrython api
            card_raw = get_png_from_scrython(card_name)
            # 2. border crop
            card_crop = border_crop(card_raw)
            # 3. black out copyright
            card_clean = black_out(card_crop)
            # 4. upscale
            card_upsaled = upscale_card(card_clean)
            # 5. downscale to right res
            card_downscaled = downscale_card(card_upscaled)
            # 6. add border
            card_final = add_border(card_downscaled)
            # save card to output directory
            save_card(card_final, card_name)
        return

    def get_png_from_scrython(card_name):
        # TODO: get png from scrython
        # input: card name to be pulled from scrython
        # output: raw scrython png (745x1040)
        return card_raw

    def border_crop(card_raw):
        # TODO: border crop image
        # input: raw scrython png (745x1040)
        # output: border cropped png (680x976)
        return

    def black_out(card_crop):
        # TODO: black out the wotc copyright
        # input: border cropped png (680x976)
        # output: blacked out png (680x976)
        return

    def upscale_card(card_clean):
        # TODO: upscale image until its high enough res
        # input: blacked out png (680x976)
        # output: upscaled png ()
        return

    def downscale_card(card_upscaled):
        # TODO: downscale res to target
        # input: upscaled png ()
        # output: downscaled png (2734x3950)
        return

    def add_border(card_downscaled):
        # TODO: adds big border to card for printing
        # input: downsized card (2734x3950)
        # output: print ready card (3288x4488)
        return
