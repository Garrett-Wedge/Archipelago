import typing

from BaseClasses import Item

offset = 251000
badgeoffset = 900

def pc_data_to_ap_id(data, event):
    # TODO: implement
    if event or data[2] is None or data[0] == 'Shop':
        return None
    offset = 251000
    if data[0] in ['Item', 'BossKey', 'Compass', 'Map', 'SmallKey', 'Token', 'GanonBossKey', 'FortressSmallKey', 'Song']:
        return offset + data[2]
    else:
        raise Exception(f'Unexpected OOT item type found: {data[0]}')

def ap_id_to_pc_data(ap_id):
    offset = 251000
    val = ap_id - offset
    if val > 900:  # this is a badge
        val = val - 900
        # TODO: implement
    try:
        return list(filter(lambda d: d[1][0] == 'Item' and d[1][2] == val, item_table.items()))[0]
    except IndexError:
        raise Exception(f'Could not find desired item ID: {ap_id}')

class PokemonCrystalItem(Item):
    game: str = "Pokemon Crystal"

    def __init__(self, name, advancement, code, player):
        super().__init__(name, advancement, code, player)
        self.name = name
        self.advancement = advancement
        self.player = player
        self.code = code
        self.type = ""
        self.kir_name = ""  # the name in the ItemValues dictionary


#    APName,               (type,        advancement, itemID, KIRName
item_table = {
    'Master Ball':			('Ball'          , False, 1  , "MASTER_BALL"),
    'Ultra Ball':			('Ball'          , False, 2  , "ULTRA_BALL"),
    'BrightPowder':			('HeldItems'     , False, 3  , "BRIGHTPOWDER"),
    'Great Ball':			('Ball'          , False, 4  , "GREAT_BALL"),
    'Poke Ball':			('Ball'          , False, 5  , "POKE_BALL"),
    'Town Map':				('Key'           , False, 6  , "TOWN_MAP"),
    'Bicycle':				('Key'           , True , 7  , "BICYCLE"),
    'Moon Stone':			('EvolutionStone', False, 8  , "MOON_STONE"),
    'Antidote':				('Healing'       , False, 9  , "ANTIDOTE"),
    'Burn Heal':			('Healing'       , False, 10 , "BURN_HEAL"),
    'Ice Heal':				('Healing'       , False, 11 , "ICE_HEAL"),
    'Awakening':			('Healing'       , False, 12 , "AWAKENING"),
    'Parlyz Heal':			('Healing'       , False, 13 , "PARLYZ_HEAL"),
    'Full Restore':			('Healing'       , False, 14 , "FULL_RESTORE"),
    'Max Potion':			('Healing'       , False, 15 , "MAX_POTION"),
    'Hyper Potion':			('Healing'       , False, 16 , "HYPER_POTION"),
    'Super Potion':			('Healing'       , False, 17 , "SUPER_POTION"),
    'Potion':				('Healing'       , False, 18 , "POTION"),
    'Escape Rope':			('OutsideBattle' , False, 19 , "ESCAPE_ROPE"),
    'Repel':				('OutsideBattle' , False, 20 , "REPEL"),
    'Max Elixer':			('Healing'       , False, 21 , "MAX_ELIXER"),
    'Fire Stone':			('EvolutionStone', False, 22 , "FIRE_STONE"),
    'ThunderStone':			('EvolutionStone', False, 23 , "THUNDERSTONE"),
    'Water Stone':			('EvolutionStone', False, 24 , "WATER_STONE"),
    'Done Button':			('AddedIn'       , False, 25 , "DONE_BUTTON"),
    'HP Up':				('OutsideBattle' , False, 26 , "HP_UP"),
    'Protein':				('OutsideBattle' , False, 27 , "PROTEIN"),
    'Iron':					('OutsideBattle' , False, 28 , "IRON"),
    'Carbos':				('OutsideBattle' , False, 29 , "CARBOS"),
    'Lucky Punch':			('MonBoosting'   , False, 30 , "LUCKY_PUNCH"),
    'Calcium':				('OutsideBattle' , False, 31 , "CALCIUM"),
    'Rare Candy':			('Healing'       , False, 32 , "RARE_CANDY"),
    'X Accuracy':			('XItems'        , False, 33 , "X_ACCURACY"),
    'Leaf Stone':			('EvolutionStone', False, 34 , "LEAF_STONE"),
    'Metal Powder':			('MonBoosting'   , False, 35 , "METAL_POWDER"),
    'Nugget':				('Valuable'      , False, 36 , "NUGGET"),
    'Poke Doll':			('Healing'       , False, 37 , "POKE_DOLL"),
    'Full Heal':			('Healing'       , False, 38 , "FULL_HEAL"),
    'Revive':				('Healing'       , False, 39 , "REVIVE"),
    'Max Revive':			('Healing'       , False, 40 , "MAX_REVIVE"),
    'Guard Spec':			('XItems'        , False, 41 , "GUARD_SPEC"),
    'Super Repel':			('OutsideBattle' , False, 42 , "SUPER_REPEL"),
    'Max Repel':			('OutsideBattle' , False, 43 , "MAX_REPEL"),
    'Dire Hit':				('XItems'        , False, 44 , "DIRE_HIT"),
    'Fresh Water':			('Healing'       , False, 46 , "FRESH_WATER"),
    'Soda Pop':				('Healing'       , False, 47 , "SODA_POP"),
    'Lemonade':				('Healing'       , False, 48 , "LEMONADE"),
    'X Attack':				('XItems'        , False, 49 , "X_ATTACK"),
    'X Defend':				('XItems'        , False, 51 , "X_DEFEND"),
    'X Speed':				('XItems'        , False, 52 , "X_SPEED"),
    'X Special':			('XItems'        , False, 53 , "X_SPECIAL"),
    'Coin Case':			('Key'           , False, 54 , "COIN_CASE"),
    'Itemfinder':			('Key'           , False, 55 , "ITEMFINDER"),
    'Poke Flute':			('Key'           , False, 56 , "POKE_FLUTE"),
    'EXP Share':			('HeldItems'     , False, 57 , "EXP_SHARE"),
    'Old Rod':				('Key'           , False, 58 , "OLD_ROD"),
    'Good Rod':				('Key'           , False, 59 , "GOOD_ROD"),
    'Silver Leaf':			('Valuable'      , False, 60 , "SILVER_LEAF"),
    'Super Rod':			('Key'           , False, 61 , "SUPER_ROD"),
    'PP Up':				('OutsideBattle' , False, 62 , "PP_UP"),
    'Ether':				('Healing'       , False, 63 , "ETHER"),
    'Max Ether':			('Healing'       , False, 64 , "MAX_ETHER"),
    'Elixer':				('Healing'       , False, 65 , "ELIXER"),
    'Red Scale':			('Key'           , False, 66 , "RED_SCALE"),
    'SecretPotion':			('Key'           , True , 67 , "SECRETPOTION"),
    'SS Ticket':			('Key'           , True , 68 , "S_S_TICKET"),
    'Mystery Egg':			('Key'           , True , 69 , "MYSTERY_EGG"),
    'Clear Bell':			('Key'           , True , 70 , "CLEAR_BELL"),
    'Silver Wing':			('Key'           , False, 71 , "SILVER_WING"),
    'Moomoo Milk':			('Healing'       , False, 72 , "MOOMOO_MILK"),
    'Quick Claw':			('HeldItems'     , False, 73 , "QUICK_CLAW"),
    'PsnCureBerry':			('Berry'         , False, 74 , "PSNCUREBERRY"),
    'Gold Leaf':			('Valuable'      , False, 75 , "GOLD_LEAF"),
    'Soft Sand':			('HeldItems'     , False, 76 , "SOFT_SAND"),
    'Sharp Beak':			('HeldItems'     , False, 77 , "SHARP_BEAK"),
    'PrzCureBerry':			('Berry'         , False, 78 , "PRZCUREBERRY"),
    'Burnt Berry':			('Berry'         , False, 79 , "BURNT_BERRY"),
    'Ice Berry':			('Berry'         , False, 80 , "ICE_BERRY"),
    'Poison Barb':			('HeldItems'     , False, 81 , "POISON_BARB"),
    'Kings Rock':			('HeldItems'     , False, 82 , "KINGS_ROCK"),
    'Bitter Berry':			('Berry'         , False, 83 , "BITTER_BERRY"),
    'Mint Berry':			('Berry'         , False, 84 , "MINT_BERRY"),
    'Red Apricorn':			('Apricorn'      , False, 85 , "RED_APRICORN"),
    'TinyMushroom':			('Valuable'      , False, 86 , "TINYMUSHROOM"),
    'Big Mushroom':			('Valuable'      , False, 87 , "BIG_MUSHROOM"),
    'SilverPowder':			('Valuable'      , False, 88 , "SILVERPOWDER"),
    'Blu Apricorn':			('Apricorn'      , False, 89 , "BLU_APRICORN"),
    'Amulet Coin':			('HeldItems'     , False, 91 , "AMULET_COIN"),
    'Ylw Apricorn':			('Apricorn'      , False, 92 , "YLW_APRICORN"),
    'Grn Apricorn':			('Apricorn'      , False, 93 , "GRN_APRICORN"),
    'Cleanse Tag':			('HeldItems'     , False, 94 , "CLEANSE_TAG"),
    'Mystic Water':			('HeldItems'     , False, 95 , "MYSTIC_WATER"),
    'TwistedSpoon':			('HeldItems'     , False, 96 , "TWISTEDSPOON"),
    'Wht Apricorn':			('Apricorn'      , False, 97 , "WHT_APRICORN"),
    'Blackbelt':			('HeldItems'     , False, 98 , "BLACKBELT"),
    'Blk Apricorn':			('Apricorn'      , False, 99 , "BLK_APRICORN"),
    'Pnk Apricorn':			('Apricorn'      , False, 101, "PNK_APRICORN"),
    'BlackGlasses':			('HeldItems'     , False, 102, "BLACKGLASSES"),
    'SlowpokeTail':			('Valuable'      , False, 103, "SLOWPOKETAIL"),
    'Pink Bow':				('HeldItems'     , False, 104, "PINK_BOW"),
    'Stick':				('MonBoosting'   , False, 105, "STICK"),
    'Smoke Ball':			('HeldItems'     , False, 106, "SMOKE_BALL"),
    'NeverMeltIce':			('HeldItems'     , False, 107, "NEVERMELTICE"),
    'Magnet':				('HeldItems'     , False, 108, "MAGNET"),
    'MiracleBerry':			('HeldItems'     , False, 109, "MIRACLEBERRY"),
    'Pearl':				('Valuable'      , False, 110, "PEARL"),
    'Big Pearl':			('Valuable'      , False, 111, "BIG_PEARL"),
    'Everstone':			('HeldItems'     , False, 112, "EVERSTONE"),
    'Spell Tag':			('HeldItems'     , False, 113, "SPELL_TAG"),
    'RageCandyBar':			('Healing'       , False, 114, "RAGECANDYBAR"),
    'GS Ball':				('Ball'          , False, 115, "GS_BALL"),
    'Blue Card':			('Key'           , False, 116, "BLUE_CARD"),
    'Miracle Seed':			('HeldItems'     , False, 117, "MIRACLE_SEED"),
    'Thick Club':			('MonBoosting'   , False, 118, "THICK_CLUB"),
    'Focus Band':			('HeldItems'     , False, 119, "FOCUS_BAND"),
    'EnergyPowder':			('Healing'       , False, 121, "ENERGYPOWDER"),
    'Energy Root':			('Healing'       , False, 122, "ENERGY_ROOT"),
    'Heal Powder':			('Healing'       , False, 123, "HEAL_POWDER"),
    'Revival Herb':			('Healing'       , False, 124, "REVIVAL_HERB"),
    'Hard Stone':			('HeldItems'     , False, 125, "HARD_STONE"),
    'Lucky Egg':			('HeldItems'     , False, 126, "LUCKY_EGG"),
    'Card Key':				('Key'           , True , 127, "CARD_KEY"),
    'Machine Part':			('Key'           , True , 128, "MACHINE_PART"),
    'Egg Ticket':			('Key'           , False, 129, "EGG_TICKET"),
    'Lost Item':			('Key'           , True , 130, "LOST_ITEM"),
    'Stardust':				('Valuable'      , False, 131, "STARDUST"),
    'Star Piece':			('Valuable'      , False, 132, "STAR_PIECE"),
    'Basement Key':			('Key'           , True , 133, "BASEMENT_KEY"),
    'Pass':					('Key'           , True , 134, "PASS"),
    'Charcoal':				('HeldItems'     , False, 138, "CHARCOAL"),
    'Berry Juice':			('HeldItems'     , False, 139, "BERRY_JUICE"),
    'Scope Lens':			('HeldItems'     , False, 140, "SCOPE_LENS"),
    'Metal Coat':			('HeldItems'     , False, 143, "METAL_COAT"),
    'Dragon Fang':			('HeldItems'     , False, 144, "DRAGON_FANG"),
    'Leftovers':			('HeldItems'     , False, 146, "LEFTOVERS"),
    'Mysteryberry':			('Berry'         , False, 150, "MYSTERYBERRY"),
    'Dragon Scale':			('HeldItems'     , False, 151, "DRAGON_SCALE"),
    'Berserk Gene':			('HeldItems'     , False, 152, "BERSERK_GENE"),
    'Sacred Ash':			('Healing'       , False, 156, "SACRED_ASH"),
    'Heavy Ball':			('Ball'          , False, 157, "HEAVY_BALL"),
    'Flower Mail':			('Mail'          , False, 158, "FLOWER_MAIL"),
    'Level Ball':			('Ball'          , False, 159, "LEVEL_BALL"),
    'Lure Ball':			('Ball'          , False, 160, "LURE_BALL"),
    'Fast Ball':			('Ball'          , False, 161, "FAST_BALL"),
    'Light Ball':			('Ball'          , False, 163, "LIGHT_BALL"),
    'Friend Ball':			('Ball'          , False, 164, "FRIEND_BALL"),
    'Moon Ball':			('Ball'          , False, 165, "MOON_BALL"),
    'Love Ball':			('Ball'          , False, 166, "LOVE_BALL"),
    'Normal Box':			('OutsideBattle' , False, 167, "NORMAL_BOX"),
    'Gorgeous Box':			('OutsideBattle' , False, 168, "GORGEOUS_BOX"),
    'Sun Stone':			('EvolutionStone', False, 169, "SUN_STONE"),
    'Polkadot Bow':			('HeldItems'     , False, 170, "POLKADOT_BOW"),
    'Up Grade':				('HeldItems'     , False, 172, "UP_GRADE"),
    'Berry':				('Berry'         , False, 173, "BERRY"),
    'Gold Berry':			('Berry'         , False, 174, "GOLD_BERRY"),
    'SquirtBottle':			('Key'           , True , 175, "SQUIRTBOTTLE"),
    'Park Ball':			('Ball'          , False, 177, "PARK_BALL"),
    'Rainbow Wing':			('Key'           , True , 178, "RAINBOW_WING"),
    'Brick Piece':			('Valuable'      , False, 180, "BRICK_PIECE"),
    'Surf Mail':			('Mail'          , False, 181, "SURF_MAIL"),
    'LiteBlueMail':			('Mail'          , False, 182, "LITEBLUEMAIL"),
    'Portraitmail':			('Mail'          , False, 183, "PORTRAITMAIL"),
    'Lovely Mail':			('Mail'          , False, 184, "LOVELY_MAIL"),
    'Eon Mail':				('Mail'          , False, 185, "EON_MAIL"),
    'Morph Mail':			('Mail'          , False, 186, "MORPH_MAIL"),
    'Bluesky Mail':			('Mail'          , False, 187, "BLUESKY_MAIL"),
    'Music Mail':			('Mail'          , False, 188, "MUSIC_MAIL"),
    'Mirage Mail':			('Mail'          , False, 189, "MIRAGE_MAIL"),
    'TM Dynamicpunch':		('TM'            , False, 191, "TM_DYNAMICPUNCH"),
    'TM Headbutt':			('TM'            , False, 192, "TM_HEADBUTT"),
    'TM Curse':				('TM'            , False, 193, "TM_CURSE"),
    'TM Rollout':			('TM'            , False, 194, "TM_ROLLOUT"),
    'TM Roar':				('TM'            , False, 196, "TM_ROAR"),
    'TM Toxic':				('TM'            , False, 197, "TM_TOXIC"),
    'TM Zap Cannon':		('TM'            , False, 198, "TM_ZAP_CANNON"),
    'TM Rock Smash':		('TM'            , False, 199, "TM_ROCK_SMASH"),
    'TM Psych Up':			('TM'            , False, 200, "TM_PSYCH_UP"),
    'TM Hidden Power':		('TM'            , False, 201, "TM_HIDDEN_POWER"),
    'TM Sunny Day':			('TM'            , False, 202, "TM_SUNNY_DAY"),
    'TM Sweet Scent':		('TM'            , False, 203, "TM_SWEET_SCENT"),
    'TM Snore':				('TM'            , False, 204, "TM_SNORE"),
    'TM Blizzard':			('TM'            , False, 205, "TM_BLIZZARD"),
    'TM Hyper Beam':		('TM'            , False, 206, "TM_HYPER_BEAM"),
    'TM Icy Wind':			('TM'            , False, 207, "TM_ICY_WIND"),
    'TM Protect':			('TM'            , False, 208, "TM_PROTECT"),
    'TM Rain Dance':		('TM'            , False, 209, "TM_RAIN_DANCE"),
    'TM Giga Drain':		('TM'            , False, 210, "TM_GIGA_DRAIN"),
    'TM Endure':			('TM'            , False, 211, "TM_ENDURE"),
    'TM Frustration':		('TM'            , False, 212, "TM_FRUSTRATION"),
    'TM Solarbeam':			('TM'            , False, 213, "TM_SOLARBEAM"),
    'TM Iron Tail':			('TM'            , False, 214, "TM_IRON_TAIL"),
    'TM Dragonbreath':		('TM'            , False, 215, "TM_DRAGONBREATH"),
    'TM Thunder':			('TM'            , False, 216, "TM_THUNDER"),
    'TM Earthquake':		('TM'            , False, 217, "TM_EARTHQUAKE"),
    'TM Return':			('TM'            , False, 218, "TM_RETURN"),
    'TM Dig':				('TM'            , False, 219, "TM_DIG"),
    'TM Item Dc':			('TM'            , False, 220, "TM_ITEM_DC"),
    'TM Psychic':			('TM'            , False, 221, "TM_PSYCHIC"),
    'TM Shadow Ball':		('TM'            , False, 222, "TM_SHADOW_BALL"),
    'TM Mud Slap':			('TM'            , False, 223, "TM_MUD_SLAP"),
    'TM Double Team':		('TM'            , False, 224, "TM_DOUBLE_TEAM"),
    'TM Ice Punch':			('TM'            , False, 225, "TM_ICE_PUNCH"),
    'TM Swagger':			('TM'            , False, 226, "TM_SWAGGER"),
    'TM Sleep Talk':		('TM'            , False, 227, "TM_SLEEP_TALK"),
    'TM Sludge Bomb':		('TM'            , False, 228, "TM_SLUDGE_BOMB"),
    'TM Sandstorm':			('TM'            , False, 229, "TM_SANDSTORM"),
    'TM Fire Blast':		('TM'            , False, 230, "TM_FIRE_BLAST"),
    'TM Swift':				('TM'            , False, 231, "TM_SWIFT"),
    'TM Defense Curl':		('TM'            , False, 232, "TM_DEFENSE_CURL"),
    'TM Thunderpunch':		('TM'            , False, 233, "TM_THUNDERPUNCH"),
    'TM Dream Eater':		('TM'            , False, 234, "TM_DREAM_EATER"),
    'TM Detect':			('TM'            , False, 235, "TM_DETECT"),
    'TM Rest':				('TM'            , False, 236, "TM_REST"),
    'TM Attract':			('TM'            , False, 237, "TM_ATTRACT"),
    'TM Thief':				('TM'            , False, 238, "TM_THIEF"),
    'TM Steel Wing':		('TM'            , False, 239, "TM_STEEL_WING"),
    'TM Fire Punch':		('TM'            , False, 240, "TM_FIRE_PUNCH"),
    'TM Fury Cutter':		('TM'            , False, 241, "TM_FURY_CUTTER"),
    'TM Nightmare':			('TM'            , False, 242, "TM_NIGHTMARE"),
    'HM Cut':				('HM'            , True , 243, "HM_CUT"),
    'HM Fly':				('HM'            , False, 244, "HM_FLY"),
    'HM Surf':				('HM'            , True , 245, "HM_SURF"),
    'HM Strength':			('HM'            , True , 246, "HM_STRENGTH"),
    'HM Flash':				('HM'            , True , 247, "HM_FLASH"),
    'HM Whirlpool':			('HM'            , True , 248, "HM_WHIRLPOOL"),
    'HM Waterfall':			('HM'            , True , 249, "HM_WATERFALL"),
    'Pokedex':				('Key'           , False, 250, "ENGINE_POKEDEX"),
    'Pokegear':				('Key'           , True , 251, "ENGINE_POKEGEAR"),
    'Radio Card':			('Key'           , False, 252, "ENGINE_RADIO_CARD"),
    'Map Card':				('Key'           , False, 253, "ENGINE_MAP_CARD"),
    'Expn Card':			('Key'           , False, 254, "ENGINE_EXPN_CARD"),
    'Unown Dex':			('Key'           , False, 255, "ENGINE_UNOWN_DEX"),
    'Zephyrbadge':			('Badge'         , True , 927, "ENGINE_ZEPHYRBADGE"),
    'Hivebadge':			('Badge'         , True , 928, "ENGINE_HIVEBADGE"),
    'Plainbadge':			('Badge'         , True , 929, "ENGINE_PLAINBADGE"),
    'Fogbadge':				('Badge'         , True , 930, "ENGINE_FOGBADGE"),
    'Mineralbadge':			('Badge'         , True , 931, "ENGINE_MINERALBADGE"),
    'Stormbadge':			('Badge'         , True , 932, "ENGINE_STORMBADGE"),
    'Glacierbadge':			('Badge'         , True , 933, "ENGINE_GLACIERBADGE"),
    'Risingbadge':			('Badge'         , True , 934, "ENGINE_RISINGBADGE"),
    'Boulderbadge':			('Badge'         , True , 935, "ENGINE_BOULDERBADGE"),
    'Cascadebadge':			('Badge'         , True , 936, "ENGINE_CASCADEBADGE"),
    'Thunderbadge':			('Badge'         , True , 937, "ENGINE_THUNDERBADGE"),
    'Rainbowbadge':			('Badge'         , True , 938, "ENGINE_RAINBOWBADGE"),
    'Soulbadge':			('Badge'         , True , 939, "ENGINE_SOULBADGE"),
    'Marshbadge':			('Badge'         , True , 940, "ENGINE_MARSHBADGE"),
    'Volcanobadge':			('Badge'         , True , 941, "ENGINE_VOLCANOBADGE"),
    'Earthbadge':			('Badge'         , True , 942, "ENGINE_EARTHBADGE")
}
