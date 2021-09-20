from pathlib import PurePosixPath

KNOWN_FONTS_V1 = [
    "Data/Fonts/fontdebug.fnb",
    "Data/Fonts/fontfirasans.fnb",
    "Data/Fonts/fontmono.fnb",
    "Data/Fonts/fontyorkten.fnb",
]

KNOWN_FONTS_V2 = [
    *KNOWN_FONTS_V1,
    "Data/Fonts/fontnewrodin.fnb",
    "Data/Fonts/fontrodincattleya.fnb",
]

KNOWN_FONTS_V3 = [
    *KNOWN_FONTS_V2,
    "Data/Fonts/fontnotosansboldcs.fnb",
    "Data/Fonts/fontnotosansboldct.fnb",
    "Data/Fonts/fontnotosansboldko.fnb",
    "Data/Fonts/fontnotosansboldnicknames.fnb",
    "Data/Fonts/fontnotosansboldru.fnb",
    "Data/Fonts/fontnotosansitaliccs.fnb",
    "Data/Fonts/fontnotosansitalicct.fnb",
    "Data/Fonts/fontnotosansitalicko.fnb",
    "Data/Fonts/fontnotosansitalicru.fnb",
]

KNOWN_LEVELS_V1 = [
    "Data/Levels/abzu.lvl",
    "Data/Levels/Arena/dm1-1.lvl",
    "Data/Levels/Arena/dm1-2.lvl",
    "Data/Levels/Arena/dm1-3.lvl",
    "Data/Levels/Arena/dm1-4.lvl",
    "Data/Levels/Arena/dm1-5.lvl",
    "Data/Levels/Arena/dm2-1.lvl",
    "Data/Levels/Arena/dm2-2.lvl",
    "Data/Levels/Arena/dm2-3.lvl",
    "Data/Levels/Arena/dm2-4.lvl",
    "Data/Levels/Arena/dm2-5.lvl",
    "Data/Levels/Arena/dm3-1.lvl",
    "Data/Levels/Arena/dm3-2.lvl",
    "Data/Levels/Arena/dm3-3.lvl",
    "Data/Levels/Arena/dm3-4.lvl",
    "Data/Levels/Arena/dm3-5.lvl",
    "Data/Levels/Arena/dm4-1.lvl",
    "Data/Levels/Arena/dm4-2.lvl",
    "Data/Levels/Arena/dm4-3.lvl",
    "Data/Levels/Arena/dm4-4.lvl",
    "Data/Levels/Arena/dm4-5.lvl",
    "Data/Levels/Arena/dm5-1.lvl",
    "Data/Levels/Arena/dm5-2.lvl",
    "Data/Levels/Arena/dm5-3.lvl",
    "Data/Levels/Arena/dm5-4.lvl",
    "Data/Levels/Arena/dm5-5.lvl",
    "Data/Levels/Arena/dm6-1.lvl",
    "Data/Levels/Arena/dm6-2.lvl",
    "Data/Levels/Arena/dm6-3.lvl",
    "Data/Levels/Arena/dm6-4.lvl",
    "Data/Levels/Arena/dm6-5.lvl",
    "Data/Levels/Arena/dm7-1.lvl",
    "Data/Levels/Arena/dm7-2.lvl",
    "Data/Levels/Arena/dm7-3.lvl",
    "Data/Levels/Arena/dm7-4.lvl",
    "Data/Levels/Arena/dm7-5.lvl",
    "Data/Levels/Arena/dm8-1.lvl",
    "Data/Levels/Arena/dm8-2.lvl",
    "Data/Levels/Arena/dm8-3.lvl",
    "Data/Levels/Arena/dm8-4.lvl",
    "Data/Levels/Arena/dm8-5.lvl",
    "Data/Levels/Arena/dmpreview.tok",
    "Data/Levels/babylonarea.lvl",
    "Data/Levels/basecamp_garden.lvl",
    "Data/Levels/basecamp.lvl",
    "Data/Levels/basecamp_shortcut_discovered.lvl",
    "Data/Levels/basecamp_shortcut_undiscovered.lvl",
    "Data/Levels/basecamp_shortcut_unlocked.lvl",
    "Data/Levels/basecamp_surface.lvl",
    "Data/Levels/basecamp_tutorial.lvl",
    "Data/Levels/basecamp_tv_room_locked.lvl",
    "Data/Levels/basecamp_tv_room_unlocked.lvl",
    "Data/Levels/beehive.lvl",
    "Data/Levels/blackmarket.lvl",
    "Data/Levels/cavebossarea.lvl",
    "Data/Levels/challenge_moon.lvl",
    "Data/Levels/challenge_star.lvl",
    "Data/Levels/challenge_sun.lvl",
    "Data/Levels/cityofgold.lvl",
    "Data/Levels/cosmicocean_babylon.lvl",
    "Data/Levels/cosmicocean_dwelling.lvl",
    "Data/Levels/cosmicocean_icecavesarea.lvl",
    "Data/Levels/cosmicocean_jungle.lvl",
    "Data/Levels/cosmicocean_sunkencity.lvl",
    "Data/Levels/cosmicocean_temple.lvl",
    "Data/Levels/cosmicocean_tidepool.lvl",
    "Data/Levels/cosmicocean_volcano.lvl",
    "Data/Levels/duat.lvl",
    "Data/Levels/dwellingarea.lvl",
    "Data/Levels/ending_hard.lvl",
    "Data/Levels/eggplantarea.lvl",
    "Data/Levels/ending.lvl",
    "Data/Levels/generic.lvl",
    "Data/Levels/hallofushabti.lvl",
    "Data/Levels/hundun.lvl",
    "Data/Levels/icecavesarea.lvl",
    "Data/Levels/junglearea.lvl",
    "Data/Levels/lake.lvl",
    "Data/Levels/lakeoffire.lvl",
    "Data/Levels/olmecarea.lvl",
    "Data/Levels/palaceofpleasure.lvl",
    "Data/Levels/sunkencityarea.lvl",
    "Data/Levels/templearea.lvl",
    "Data/Levels/testingarea.lvl",
    "Data/Levels/tiamat.lvl",
    "Data/Levels/tidepoolarea.lvl",
    "Data/Levels/vladscastle.lvl",
    "Data/Levels/volcanoarea.lvl",
]

KNOWN_LEVELS_V2 = [
    *KNOWN_LEVELS_V1,
    "Data/Levels/babylonarea_1-1.lvl",
]

KNOWN_STRINGS_V1 = [
    "strings00.str",
    "strings01.str",
    "strings02.str",
    "strings03.str",
    "strings04.str",
    "strings05.str",
    "strings06.str",
    "strings07.str",
]

KNOWN_STRINGS_V2 = [
    *KNOWN_STRINGS_V1,
    "strings08.str",
]

KNOWN_STRINGS_V3 = [
    *KNOWN_STRINGS_V2,
    "strings09.str",
    "strings10.str",
    "strings11.str",
    "strings12.str",
]

KNOWN_TEXTURES_V1 = [
    "Data/Textures/base_eggship2.png",
    "Data/Textures/base_eggship3.png",
    "Data/Textures/base_eggship.png",
    "Data/Textures/base_skynight.png",
    "Data/Textures/base_surface2.png",
    "Data/Textures/base_surface.png",
    "Data/Textures/bayer8.png",
    "Data/Textures/bg_babylon.png",
    "Data/Textures/bg_beehive.png",
    "Data/Textures/bg_cave.png",
    "Data/Textures/bg_duat2.png",
    "Data/Textures/bg_duat.png",
    "Data/Textures/bg_eggplant.png",
    "Data/Textures/bg_gold.png",
    "Data/Textures/bg_ice.png",
    "Data/Textures/bg_jungle.png",
    "Data/Textures/bg_mothership.png",
    "Data/Textures/bg_stone.png",
    "Data/Textures/bg_sunken.png",
    "Data/Textures/bg_temple.png",
    "Data/Textures/bg_tidepool.png",
    "Data/Textures/bg_vlad.png",
    "Data/Textures/bg_volcano.png",
    "Data/Textures/border_main.png",
    "Data/Textures/char_black.png",
    "Data/Textures/char_blue.png",
    "Data/Textures/char_cerulean.png",
    "Data/Textures/char_cinnabar.png",
    "Data/Textures/char_cyan.png",
    "Data/Textures/char_eggchild.png",
    "Data/Textures/char_gold.png",
    "Data/Textures/char_gray.png",
    "Data/Textures/char_green.png",
    "Data/Textures/char_hired.png",
    "Data/Textures/char_iris.png",
    "Data/Textures/char_khaki.png",
    "Data/Textures/char_lemon.png",
    "Data/Textures/char_lime.png",
    "Data/Textures/char_magenta.png",
    "Data/Textures/char_olive.png",
    "Data/Textures/char_orange.png",
    "Data/Textures/char_pink.png",
    "Data/Textures/char_red.png",
    "Data/Textures/char_violet.png",
    "Data/Textures/char_white.png",
    "Data/Textures/char_yellow.png",
    "Data/Textures/coffins.png",
    "Data/Textures/credits.png",
    "Data/Textures/deco_babylon.png",
    "Data/Textures/deco_basecamp.png",
    "Data/Textures/deco_cave.png",
    "Data/Textures/deco_cosmic.png",
    "Data/Textures/deco_eggplant.png",
    "Data/Textures/deco_extra.png",
    "Data/Textures/deco_gold.png",
    "Data/Textures/deco_ice.png",
    "Data/Textures/deco_jungle.png",
    "Data/Textures/deco_sunken.png",
    "Data/Textures/deco_temple.png",
    "Data/Textures/deco_tidepool.png",
    "Data/Textures/deco_tutorial.png",
    "Data/Textures/deco_volcano.png",
    "Data/Textures/floor_babylon.png",
    "Data/Textures/floor_cave.png",
    "Data/Textures/floor_eggplant.png",
    "Data/Textures/floor_ice.png",
    "Data/Textures/floor_jungle.png",
    "Data/Textures/floormisc.png",
    "Data/Textures/floorstyled_babylon.png",
    "Data/Textures/floorstyled_beehive.png",
    "Data/Textures/floorstyled_duat.png",
    "Data/Textures/floorstyled_gold_normal.png",
    "Data/Textures/floorstyled_gold.png",
    "Data/Textures/floorstyled_guts.png",
    "Data/Textures/floorstyled_mothership.png",
    "Data/Textures/floorstyled_pagoda.png",
    "Data/Textures/floorstyled_palace.png",
    "Data/Textures/floorstyled_stone.png",
    "Data/Textures/floorstyled_sunken.png",
    "Data/Textures/floorstyled_temple.png",
    "Data/Textures/floorstyled_vlad.png",
    "Data/Textures/floorstyled_wood.png",
    "Data/Textures/floor_sunken.png",
    "Data/Textures/floor_surface.png",
    "Data/Textures/floor_temple.png",
    "Data/Textures/floor_tidepool.png",
    "Data/Textures/floor_volcano.png",
    "Data/Textures/fontdebug.png",
    "Data/Textures/fontfirasans.png",
    "Data/Textures/fontmono.png",
    "Data/Textures/fontnewrodin.png",
    "Data/Textures/fontrodincattleya.png",
    "Data/Textures/fontyorkten.png",
    "Data/Textures/fx_ankh.png",
    "Data/Textures/fx_big.png",
    "Data/Textures/fx_explosion.png",
    "Data/Textures/fx_rubble.png",
    "Data/Textures/fx_small2.png",
    "Data/Textures/fx_small3.png",
    "Data/Textures/fx_small.png",
    "Data/Textures/hud_controller_buttons.png",
    "Data/Textures/hud.png",
    "Data/Textures/hud_text.png",
    "Data/Textures/items.png",
    "Data/Textures/items_ushabti.png",
    "Data/Textures/journal_back.png",
    "Data/Textures/journal_elements.png",
    "Data/Textures/journal_entry_bg.png",
    "Data/Textures/journal_entry_items.png",
    "Data/Textures/journal_entry_mons_big.png",
    "Data/Textures/journal_entry_mons.png",
    "Data/Textures/journal_entry_people.png",
    "Data/Textures/journal_entry_place.png",
    "Data/Textures/journal_entry_traps.png",
    "Data/Textures/journal_pageflip.png",
    "Data/Textures/journal_pagetorn.png",
    "Data/Textures/journal_select.png",
    "Data/Textures/journal_stickers.png",
    "Data/Textures/journal_story.png",
    "Data/Textures/journal_top_entry.png",
    "Data/Textures/journal_top_gameover.png",
    "Data/Textures/journal_top_main.png",
    "Data/Textures/journal_top_profile.png",
    "Data/Textures/loading.png",
    "Data/Textures/lut_backlayer.png",
    "Data/Textures/lut_blackmarket.png",
    "Data/Textures/lut_icecaves.png",
    "Data/Textures/lut_original.png",
    "Data/Textures/lut_vlad.png",
    "Data/Textures/main_body.png",
    "Data/Textures/main_dirt.png",
    "Data/Textures/main_doorback.png",
    "Data/Textures/main_doorframe.png",
    "Data/Textures/main_door.png",
    "Data/Textures/main_fore1.png",
    "Data/Textures/main_fore2.png",
    "Data/Textures/main_head.png",
    "Data/Textures/menu_basic.png",
    "Data/Textures/menu_brick1.png",
    "Data/Textures/menu_brick2.png",
    "Data/Textures/menu_cave1.png",
    "Data/Textures/menu_cave2.png",
    "Data/Textures/menu_chardoor.png",
    "Data/Textures/menu_charsel.png",
    "Data/Textures/menu_deathmatch2.png",
    "Data/Textures/menu_deathmatch3.png",
    "Data/Textures/menu_deathmatch4.png",
    "Data/Textures/menu_deathmatch5.png",
    "Data/Textures/menu_deathmatch6.png",
    "Data/Textures/menu_deathmatch.png",
    "Data/Textures/menu_disp.png",
    "Data/Textures/menu_generic.png",
    "Data/Textures/menu_header.png",
    "Data/Textures/menu_leader.png",
    "Data/Textures/menu_online.png",
    "Data/Textures/menu_titlegal.png",
    "Data/Textures/menu_title.png",
    "Data/Textures/menu_tunnel.png",
    "Data/Textures/monsters01.png",
    "Data/Textures/monsters02.png",
    "Data/Textures/monsters03.png",
    "Data/Textures/monstersbasic01.png",
    "Data/Textures/monstersbasic02.png",
    "Data/Textures/monstersbasic03.png",
    "Data/Textures/monstersbig01.png",
    "Data/Textures/monstersbig02.png",
    "Data/Textures/monstersbig03.png",
    "Data/Textures/monstersbig04.png",
    "Data/Textures/monstersbig05.png",
    "Data/Textures/monstersbig06.png",
    "Data/Textures/monsters_ghost.png",
    "Data/Textures/monsters_hundun.png",
    "Data/Textures/monsters_olmec.png",
    "Data/Textures/monsters_osiris.png",
    "Data/Textures/monsters_pets.png",
    "Data/Textures/monsters_tiamat.png",
    "Data/Textures/monsters_yama.png",
    "Data/Textures/mounts.png",
    "Data/Textures/noise0.png",
    "Data/Textures/noise1.png",
    "Data/Textures/OldTextures/ai.png",
    "Data/Textures/saving.png",
    "Data/Textures/shadows.png",
    "Data/Textures/shine.png",
    "Data/Textures/splash0.png",
    "Data/Textures/splash1.png",
    "Data/Textures/splash2.png",
]

KNOWN_TEXTURES_V2 = [
    str(PurePosixPath(path).with_suffix(".DDS")) for path in KNOWN_TEXTURES_V1
]

KNOWN_TEXTURES_V3 = [
    *KNOWN_TEXTURES_V2,
    "Data/Textures/fontnotosansboldcs_0.DDS",
    "Data/Textures/fontnotosansboldct_0.DDS",
    "Data/Textures/fontnotosansboldko_0.DDS",
    "Data/Textures/fontnotosansboldnicknames_0.DDS",
    "Data/Textures/fontnotosansboldru_0.DDS",
    "Data/Textures/fontnotosansitaliccs_0.DDS",
    "Data/Textures/fontnotosansitalicct_0.DDS",
    "Data/Textures/fontnotosansitalicko_0.DDS",
    "Data/Textures/fontnotosansitalicru_0.DDS",
]

KNOWN_FILEPATHS = [
    *KNOWN_FONTS_V3,
    *KNOWN_LEVELS_V2,
    *KNOWN_STRINGS_V3,
    *KNOWN_TEXTURES_V3,
    # Shaders
    "shaders.hlsl",
    # FMOD Audio
    "soundbank.bank",
    "soundbank.strings.bank",
]


# Mapping of filenames to their file paths
# Example: {'splash1.DDS': 'Data/Textures/splash1.DDS'}
FILENAMES_TO_FILEPATHS = {PurePosixPath(path).name: path for path in KNOWN_FILEPATHS}

# Most of the textures convert cleanly to .png but not all of them.
# This is the list of assets we want to convert to/from png.
DDS_PNGS = set(
    asset
    for asset in KNOWN_TEXTURES_V2
    if asset
    not in [
        "Data/Textures/bayer8.DDS",
        "Data/Textures/fontdebug.DDS",
        "Data/Textures/fontfirasans.DDS",
        "Data/Textures/fontmono.DDS",
        "Data/Textures/fontnewrodin.DDS",
        "Data/Textures/fontrodincattleya.DDS",
        "Data/Textures/fontyorkten.DDS",
    ]
)


# Mapping of png file names to DDS file names
# Example: {'monstersbig06.png': 'monstersbig06.DDS'}
PNG_NAMES_TO_DDS_NAMES = {
    str(PurePosixPath(filepath).with_suffix(".png").name): str(
        PurePosixPath(filepath).name
    )
    for filepath in KNOWN_TEXTURES_V2
    if filepath in DDS_PNGS
}

EXTRACTED_DIR = PurePosixPath("Extracted")
PACKS_DIR = PurePosixPath("Packs")

FILEPATH_DIRS = [
    PurePosixPath(path).parent
    for path in KNOWN_FILEPATHS
    if PurePosixPath(path).parent != PurePosixPath(".")
]

DEFAULT_COMPRESSION_LEVEL = 20
BANK_ALIGNMENT = 32
