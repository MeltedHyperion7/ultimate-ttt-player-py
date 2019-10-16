#!/bin/bash

from abc import ABCMeta,

from engine import MainBoardCoords, SubBoardCoords
from engine.main_board import MainBoard
from stdout import StdOutPlayer


class UltimatePlayer(StdOutPlayer):
    def __init__(self):
        self.board_size = 3
        self.main_board = MainBoard(self.board_size)

    
    def onMove(self):
        pass
    
    
    # def afterAbhijay(self, board, move):
    #     for row in range(3):
    #         for column in range(3):
    #             subBoard = MainBoardCoords(row,column)
    #             getSub_state(subBoard)
        
    def getSub_state(self, board):
        counter = 0
        empty_counter = 0
        winning_col = 0
        diagonal_counter = 0
        diagonal_counter_empty = 0
        for row in range(3):
            for column in range(3):
                cell = self.main_board.get_sub_board(board).get_cell(SubBoardCoords(row,column))
                if cell == 2:
                    counter +=1
                elif cell == 0:
                    emtpy_counter += 1
            if counter == 2 and empty_counter == 1:
                counter = 0 
                empty_counter = 0
                return 1
            else: 
                counter = 0
                empty_counter = 0
                continue
        for column in range(3):
            for row in range(3):
                cell = self.main_board.get_sub_board(board).get_cell(SubBoardCoords(row,column))
                if cell == 2:
                    counter +=1
                elif cell == 0:
                    empty_counter == 0
            if counter == 2 and empty_counter == 1:
                counter = 0
                empty_counter = 1
                return 1
            else:
                counter = 0
                empty_counter = 0
                continue
        for row in range(3):
            column = row
            cell = self.main_board.get_sub_board(board).get_cell(SubBoardCoords(row,column))
            if cell == 2:
                counter +=1
            elif cell ==0:
                empty_counter == 0
        if diagonal_counter == 2 and diagonal_counter_empty == 1:
            diagonal_counter_empty = 0
            diagonal_counter = 0
            return 1
        else: 
            diagonal_counter = 0
            diagonal_counter_empty = 0
            continue
        for row in range(2,-1,-1):
            for column in range(3):
                cell = self.main_board.get_sub_board(board).get_cell(SubBoardCoords(row,column))
                if cell == 2:
                    counter +=1
                elif cell == 0:
                    empty_counter +=1
            if counter == 2 and empty_counter == 1:
                counter = 0
                empty_counter = 0
                return 1
            else:
                counter = 0
                empty_counter = 0
                continue
        return 0
        


        



        

    
    def gameOver(self, result, board, move):
        pass

    
    def matchOver(self, result):
        pass
    
    
    def timeout(self):
        pass

    @property
    def is_game_finished(self) -> bool:
        return self.main_board.is_finished

    def add_my_move(self, main_board_coords: MainBoardCoords, sub_board_coords: SubBoardCoords) -> None:
        self.main_board = self.main_board.add_my_move(main_board_coords, sub_board_coords)

    def add_opponent_move(self, main_board_coords: MainBoardCoords, sub_board_coords: SubBoardCoords) -> None:
        self.main_board = self.main_board.add_opponent_move(main_board_coords, sub_board_coords)
