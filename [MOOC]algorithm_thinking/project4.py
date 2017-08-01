#!/usr/bin/python
#Filename: project4.py
"""
This program uses to complete the project4 of Algorithm thinking.
"""

#general imports
from collections import deque

def build_scoring_matrix(alphabet, diag_score, \
        off_diag_score, dash_score):
    """
    Function builds a scoring matrix.
    Input: a set of characters alphabet\
            three scores: diag_score, off_diag_score, dash_score.
    Return: a dictionary of dictionaries whose entries are indexed\
            by pairs of characters in alphabet plus '-'.
    """
    whole_alphabet = alphabet.copy()
    whole_alphabet.add('-')
    scoring_matrix = {}
    for low_char in whole_alphabet:
        scoring_matrix[low_char] = {}
        for col_char in whole_alphabet:
            if low_char != '-' and col_char != '-':
                if low_char == col_char:
                    scoring_matrix[low_char][col_char] = diag_score
                else:
                    scoring_matrix[low_char][col_char] = off_diag_score
            else:
                scoring_matrix[low_char][col_char] = dash_score
    return scoring_matrix

def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Function computes alignment matrix for Global or partial alignment.
    Input: two sequences seq_x and seq_y whose elements share a common\
            alphabet with the scoring_matrix\
            global_flag is boolean syntax.
    Output: a list of lists.
    """
    len_x = len(seq_x)
    len_y = len(seq_y)
    alignment_matrix = [[dummy_y for dummy_y in xrange(len_y+1)] \
            for dummy_x in xrange(len_x+1)]
    alignment_matrix[0][0] = 0
    if len_x:
        for dummy_x in xrange(1, len_x+1):
            alignment_matrix[dummy_x][0] = alignment_matrix[dummy_x-1][0] + \
                                           scoring_matrix[seq_x[dummy_x-1]]['-']
            if global_flag == False and alignment_matrix[dummy_x][0] < 0:
                    alignment_matrix[dummy_x][0] = 0
    if len_y:
        for dummy_y in xrange(1, len_y+1):
            alignment_matrix[0][dummy_y] = alignment_matrix[0][dummy_y-1] + \
                                           scoring_matrix[seq_y[dummy_y-1]]['-']
            if global_flag == False and alignment_matrix[0][dummy_y]:
                alignment_matrix[0][dummy_y] = 0
    for dummy_x in xrange(1, len_x+1):
        for dummy_y in xrange(1, len_y+1):
            alignment_matrix[dummy_x][dummy_y] = max(\
                alignment_matrix[dummy_x - 1][dummy_y - 1] +\
                scoring_matrix[seq_x[dummy_x - 1]][seq_y[dummy_y - 1]],\
                alignment_matrix[dummy_x - 1][dummy_y] + \
                scoring_matrix[seq_x[dummy_x - 1]]['-'],\
                alignment_matrix[dummy_x][dummy_y-1] + \
                scoring_matrix['-'][seq_y[dummy_y - 1]])
            if global_flag == False and alignment_matrix[dummy_x][dummy_y] < 0:
                alignment_matrix[dummy_x][dummy_y] = 0
    return alignment_matrix

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Function computes the global alignment of seq_x and seq_y.
    Input: two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix.
    Return: a tuple (score, align_x, align_y) where score is the score of the
    optimal local alignment align_x and align_y.
    """
    align_x = deque()
    align_y = deque()

    dummy_x = 0
    dummy_y = 0
    for dummy_1 in xrange(1, len(seq_x)+1):
        for dummy_2 in xrange(1, len(seq_y)+1):
            if alignment_matrix[dummy_1][dummy_2] > alignment_matrix[dummy_x][dummy_y]:
                dummy_x = dummy_1
                dummy_y = dummy_2

    while alignment_matrix[dummy_x][dummy_y] > 0:
        if alignment_matrix[dummy_x][dummy_y] == \
                alignment_matrix[dummy_x-1][dummy_y-1] + \
                        scoring_matrix[seq_x[dummy_x-1]][seq_y[dummy_y-1]]:
            align_x.appendleft(seq_x[dummy_x-1])
            align_y.appendleft(seq_y[dummy_y-1])
            dummy_x -= 1
            dummy_y -= 1
        else:
            if alignment_matrix[dummy_x][dummy_y] == \
                            alignment_matrix[dummy_x-1][dummy_y] + \
                            scoring_matrix[seq_x[dummy_x-1]]['-']:
                align_x.appendleft(seq_x[dummy_x-1])
                align_y.appendleft('-')
                dummy_x -= 1
            else:
                align_x.appendleft('-')
                align_y.appendleft(seq_y[dummy_y - 1])
                dummy_y -= 1

    score = 0
    for dummy_x in xrange(len(align_x)):
        score += scoring_matrix[align_x[dummy_x]][align_y[dummy_x]]

    align_x_set = ''
    for element in align_x:
        align_x_set = align_x_set + element
    align_y_set = ''
    for element in align_y:
        align_y_set = align_y_set + element

    return (score, align_x_set, align_y_set)

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    Function computes the global alignment of seq_x and seq_y.
    Input: two sequences seq_x and seq_y whose elements share a common alphabet
    with the scoring matrix.
    Return: a tuple (score, align_x, align_y) where score is the score of the
    optimal local alignment align_x and align_y.
    """
    dummy_x = len(seq_x)
    dummy_y = len(seq_y)
    align_x = deque()
    align_y = deque()
    while dummy_x != 0 and dummy_y != 0:
        if alignment_matrix[dummy_x][dummy_y] == \
                alignment_matrix[dummy_x-1][dummy_y-1] + \
                        scoring_matrix[seq_x[dummy_x-1]][seq_y[dummy_y-1]]:
            align_x.appendleft(seq_x[dummy_x-1])
            align_y.appendleft(seq_y[dummy_y-1])
            dummy_x -= 1
            dummy_y -= 1
        else:
            if alignment_matrix[dummy_x][dummy_y] == \
                            alignment_matrix[dummy_x-1][dummy_y] + \
                            scoring_matrix[seq_x[dummy_x-1]]['-']:
                align_x.appendleft(seq_x[dummy_x-1])
                align_y.appendleft('-')
                dummy_x -= 1
            else:
                align_x.appendleft('-')
                align_y.appendleft(seq_y[dummy_y - 1])
                dummy_y -= 1
    
    while dummy_x != 0:
        align_x.appendleft(seq_x[dummy_x - 1])
        align_y.appendleft('-')
        dummy_x -= 1

    while dummy_y != 0:
        align_x.appendleft('-')
        align_y.appendleft(seq_y[dummy_y - 1])
        dummy_y -= 1

    score = 0
    for dummy_x in xrange(len(align_x)):
        score += scoring_matrix[align_x[dummy_x]][align_y[dummy_x]]

    align_x_set = ''
    for element in align_x:
        align_x_set = align_x_set + element
    align_y_set = ''
    for element in align_y:
        align_y_set = align_y_set + element

    return (score, align_x_set, align_y_set)

        
if __name__ == '__main__':
    ##test your data here
    #SCORING_MATRIX = build_scoring_matrix(set(['A', 'C', 'T', 'G']), 6, 2, -4)
    #print 'SCORING_MATRIX=', SCORING_MATRIX
    #ALIGNMENT_MATRIX = compute_alignment_matrix('ACG', 'ACGTT', SCORING_MATRIX, 1)
    #print 'ALIGNMENT_MATRIX=',ALIGNMENT_MATRIX
    print compute_local_alignment('abddcdeffgh', 'aabcddefghij', {'-': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'a': {'-': -1, 'a': 2, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'c': {'-': -1, 'a': -1, 'c': 2, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'b': {'-': -1, 'a': -1, 'c': -1, 'b': 2, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'e': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': 2, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'd': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': 2, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'g': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': 2, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'f': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': 2, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'i': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': 2, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'h': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': 2, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'k': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': 2, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'j': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': 2, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'm': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': 2, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'l': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': 2, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'o': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': 2, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'n': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': 2, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'q': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': 2, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'p': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': 2, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 's': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': 2, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'r': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': 2, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'u': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': 2, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 't': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': 2, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'w': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': 2, 'v': -1, 'y': -1, 'x': -1, 'z': -1}, 'v': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': 2, 'y': -1, 'x': -1, 'z': -1}, 'y': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': 2, 'x': -1, 'z': -1}, 'x': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': 2, 'z': -1}, 'z': {'-': -1, 'a': -1, 'c': -1, 'b': -1, 'e': -1, 'd': -1, 'g': -1, 'f': -1, 'i': -1, 'h': -1, 'k': -1, 'j': -1, 'm': -1, 'l': -1, 'o': -1, 'n': -1, 'q': -1, 'p': -1, 's': -1, 'r': -1, 'u': -1, 't': -1, 'w': -1, 'v': -1, 'y': -1, 'x': -1, 'z': 2}}, [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 1, 4, 3, 2, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 3, 3, 5, 4, 3, 2, 1, 0, 0, 0], [0, 0, 0, 2, 2, 5, 7, 6, 5, 4, 3, 2, 1], [0, 0, 0, 1, 4, 4, 6, 6, 5, 4, 3, 2, 1], [0, 0, 0, 0, 3, 6, 6, 5, 5, 4, 3, 2, 1], [0, 0, 0, 0, 2, 5, 5, 8, 7, 6, 5, 4, 3], [0, 0, 0, 0, 1, 4, 4, 7, 10, 9, 8, 7, 6], [0, 0, 0, 0, 0, 3, 3, 6, 9, 9, 8, 7, 6], [0, 0, 0, 0, 0, 2, 2, 5, 8, 11, 10, 9, 8], [0, 0, 0, 0, 0, 1, 1, 4, 7, 10, 13, 12, 11]])