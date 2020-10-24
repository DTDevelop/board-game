####line 133 - 157; positioning for each person moving

import simplegui
import random
import user47_L4QFIY8XDkrteLv as char

TILE_RANGE = 23

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
border = 50

BOARD_WIDTH = CANVAS_WIDTH/2 - border
BOARD_HEIGHT = CANVAS_HEIGHT/2 - border
board_center = (CANVAS_WIDTH/2, CANVAS_HEIGHT/2)

HALF_TILE_WIDTH = 25
HALF_TILE_HEIGHT = 25
tile_center = (50,50)

##### tile events
get_money = [0,3,6,9,12,15,18,21]
pay_money = [1,4,7,10,13,16,19,22]

def draw_handler(canvas):
    """
    board game draw handler
    game logic manipulated here
    """
    
    ##### drawing back of board
    board_topleft = (board_center[0]-BOARD_WIDTH, board_center[1]-BOARD_HEIGHT)
    board_topright = (board_center[0]+BOARD_WIDTH, board_center[1]-BOARD_HEIGHT)
    board_bottomright = (board_center[0]+BOARD_WIDTH, board_center[1]+BOARD_HEIGHT)
    board_bottomleft = (board_center[0]-BOARD_WIDTH, board_center[1]+BOARD_HEIGHT)

    canvas.draw_polygon([board_topleft,
                         board_topright,
                         board_bottomright,
                         board_bottomleft],
                         10, "black", "brown")
    
    ##### -- 
    
    ##### drawing tile connective tubes
    inner_decrement = 50
    inner_board_topleft = (board_center[0]-(BOARD_WIDTH-inner_decrement), board_center[1]-(BOARD_HEIGHT-inner_decrement))
    inner_board_topright = (board_center[0]+(BOARD_WIDTH-inner_decrement), board_center[1]-(BOARD_HEIGHT-inner_decrement))
    inner_board_bottomright = (board_center[0]+(BOARD_WIDTH-inner_decrement), board_center[1]+(BOARD_HEIGHT-inner_decrement))
    inner_board_bottomleft = (board_center[0]-(BOARD_WIDTH-inner_decrement), board_center[1]+(BOARD_HEIGHT-inner_decrement))

    canvas.draw_polygon([inner_board_topleft,
                         inner_board_topright,
                         inner_board_bottomright,
                         inner_board_bottomleft],
                         10, "black", "brown")    

    ##### --
    
    ##### drawing inner board
    inner_decrement = 100
    inner_board_topleft = (board_center[0]-(BOARD_WIDTH-inner_decrement), board_center[1]-(BOARD_HEIGHT-inner_decrement))
    inner_board_topright = (board_center[0]+(BOARD_WIDTH-inner_decrement), board_center[1]-(BOARD_HEIGHT-inner_decrement))
    inner_board_bottomright = (board_center[0]+(BOARD_WIDTH-inner_decrement), board_center[1]+(BOARD_HEIGHT-inner_decrement))
    inner_board_bottomleft = (board_center[0]-(BOARD_WIDTH-inner_decrement), board_center[1]+(BOARD_HEIGHT-inner_decrement))

    canvas.draw_polygon([inner_board_topleft,
                         inner_board_topright,
                         inner_board_bottomright,
                         inner_board_bottomleft],
                         4, "Teal", "Olive")     
    
    
    ##### --
    
    ##### drawing outer tiles
    tile_topleft = (tile_center[0]-HALF_TILE_WIDTH, tile_center[1]-HALF_TILE_HEIGHT)
    tile_topright = (tile_center[0]+HALF_TILE_WIDTH, tile_center[1]-HALF_TILE_HEIGHT)
    tile_bottomright = (tile_center[0]+HALF_TILE_WIDTH, tile_center[1]+HALF_TILE_HEIGHT)
    tile_bottomleft = (tile_center[0]-HALF_TILE_WIDTH, tile_center[1]+HALF_TILE_HEIGHT)
          
    num_tiles = 7
    tile_inc = 0
    center = board_topleft[0]
    for i in range(num_tiles): #top row of tiles
        canvas.draw_polygon([(tile_topleft[0] + center + tile_inc, tile_topleft[1] + center),
                             (tile_topright[0] + center + tile_inc, tile_topright[1] + center),
                             (tile_bottomright[0] + center + tile_inc, tile_bottomright[1] + center),
                             (tile_bottomleft[0] + center + tile_inc, tile_bottomleft[1] + center)],
                             5, "black", "Aqua")
       
        tile_inc += HALF_TILE_WIDTH*2 + 17
    right_column_center = tile_inc - (HALF_TILE_WIDTH*2 + 17) #center point for right column
    tile_inc = 0
    
    for i in range(num_tiles): #left column of tiles
        canvas.draw_polygon([(tile_topleft[0] + center, tile_topleft[1] + center + tile_inc),
                             (tile_topright[0] + center, tile_topright[1] + center + tile_inc),
                             (tile_bottomright[0] + center, tile_bottomright[1] + center + tile_inc),
                             (tile_bottomleft[0] + center, tile_bottomleft[1] + center + tile_inc)],
                             5, "black", "Aqua")
       
        tile_inc += HALF_TILE_WIDTH*2 + 17
    bottom_row_center = tile_inc - (HALF_TILE_WIDTH*2 + 17) #center point for bottom row
    tile_inc = 0
    
    for i in range(num_tiles): #right column of tiles
        canvas.draw_polygon([(tile_topleft[0] + center + right_column_center, tile_topleft[1] + center + tile_inc),
                             (tile_topright[0] + center + right_column_center, tile_topright[1] + center + tile_inc),
                             (tile_bottomright[0] + center + right_column_center, tile_bottomright[1] + center + tile_inc),
                             (tile_bottomleft[0] + center + right_column_center, tile_bottomleft[1] + center + tile_inc)],
                             5, "black", "Aqua")
        
        tile_inc += HALF_TILE_WIDTH*2 + 17
    tile_inc = 0
    
    for i in range(num_tiles): #bottom row of tiles
        canvas.draw_polygon([(tile_topleft[0] + center + tile_inc, tile_topleft[1] + center + bottom_row_center),
                             (tile_topright[0] + center + tile_inc, tile_topright[1] + center + bottom_row_center),
                             (tile_bottomright[0] + center + tile_inc, tile_bottomright[1] + center + bottom_row_center),
                             (tile_bottomleft[0] + center + tile_inc, tile_bottomleft[1] + center + bottom_row_center)],
                             5, "black", "Aqua")
       
        tile_inc += HALF_TILE_WIDTH*2 + 17
    
    
    ##### --
    
    ##### drawing player markers
    
    #do same as above, get fixed location for each Player marker
    #multiply increment by player tile to find new location
    for person in player_list:
        current_tile = person.get_tile()
        name = person.get_name()+1
        tile_inc = (HALF_TILE_WIDTH*2 + 17) * current_tile
        if name == 1:
            sect = (8, 15)
        elif name == 2:
            sect = (32, 15)
        elif name == 3:
            sect = (8, 32)
        else:
            sect = (32, 32) #section tiles
        if current_tile in range(0,7):
            corner = (tile_topleft[0] + center + tile_inc + sect[0], tile_topleft[1] + center + sect[1])
            canvas.draw_text('P'+str(name), corner, 12, 'black', 'monospace')
            
        elif current_tile in range(7,13):
            corner = (tile_topleft[0] + center + right_column_center + sect[0], tile_topleft[1] + center + tile_inc + sect[0])
            canvas.draw_text('P'+str(name), corner, 12, 'black', 'monospace')
            
        elif current_tile in range(13,19):
            pass
        else:
            pass
    
    
    ##### --

    
##### button handlers

def dice_bh():
    """
    dice button handler
    """
    global has_rolled
    #changes given players tile number
    
    if has_rolled:
        print 'Player', player_turn.get_name()+1, 'has already rolled!'
        return
    
    roll = random.randint(1, 6)
    current_tile = player_turn.get_tile()
    new_tile = current_tile+roll
    
    if new_tile > TILE_RANGE:
        new_tile -= TILE_RANGE
        
    player_turn.change_tile(new_tile)
    print 'Player', player_turn.get_name()+1, 'rolled a', roll
    
    has_rolled = True
    tile_event(player_turn)
    update_labels()
    return 'Player rolled ', roll 

def stats_bh():
    """
    stats button handler
    """
    for person in player_list:
        print ''
        print 'Player ', person.get_name()+1, 'has', person.get_cash(), 'dollars'
        print person.get_cash(), 'dollars'
        print len(person.get_houses()), 'houses'
    print ''
    
def end_turn_bh():
    """
    ends turn, moves to next player turn
    """
    global player_turn, has_rolled, turn_count
    
    if not has_rolled:
        print 'Please roll before ending your turn'
        return
    
    current = player_turn.get_name()
    if current == player_list[-1].get_name():
        player_turn = player_list[0]
    else:
        player_turn = player_list[current+1]
        turn_count +=1 #increment turn count
    
    print 'Player', current+1, 'has ended their turn.'
    print '\n'
    print 'Player', player_turn.get_name()+1, ', begin your turn!'
    has_rolled = False
    
    update_labels()
    

##### --

##### Helper Functions

def tile_event(player):
    """
    causes event action to occur
    """
    tile_check = player.get_tile()
    if tile_check in get_money:
        player.deposit_cash(8)
        print 'You have gained $8!'
    elif tile_check in pay_money:
        player.withdraw_cash(3)
        print 'You lost $3!'
    else:
        print 'House event! UNDER CONSTRUCTION'


##### -- create characters, start game
turn_count = 1
num_players = 4
player_list = []
has_rolled = False

for i in range(num_players):
    player = char.Character(i, 25)
    player_list.append(player)

player_turn = player_list[0] #if current turn == player_list[-1], turn to p[0]
    
frame = simplegui.create_frame('Testing', CANVAS_WIDTH, CANVAS_HEIGHT)

frame.set_canvas_background('Green')
frame.set_draw_handler(draw_handler)

button_1 = frame.add_button('Roll Dice', dice_bh)
button_2 = frame.add_button('Check Stats', stats_bh)
button_3 = frame.add_button('End Turn', end_turn_bh)


#####
frame.add_label('')
label1 = frame.add_label('PLAYER ' + str(player_turn.get_name() + 1))
label2 = frame.add_label('Cash: ' + str(player_turn.get_cash()))
label3 = frame.add_label('Houses: ')
label4 = frame.add_label('Items: ')
label5 = frame.add_label('Traits: ')

##### --

##### More helper functions
def update_labels():
    """
    update labels on status menu
    """
    frame.add_label('')
    label1.set_text('PLAYER ' + str(player_turn.get_name() +1))
    label2.set_text('Cash: ' + str(player_turn.get_cash()))
    label3.set_text('Houses: ')
    label4.set_text('Items: ')
    label5.set_text('Traits: ')
    

frame.start()







