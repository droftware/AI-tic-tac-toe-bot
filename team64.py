class Player64:

	def __init__(self):
		self.depth = 0
		pass

	def move(self,temp_board,temp_block,old_move,flag):
		#List of permitted blocks, based on old move.
		blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
		#Get list of empty valid cells
		cells = get_empty_out_of(temp_board, blocks_allowed)
		current_board_state = temp_board[:]
		current_block_state = temp_block[:]
		return minimax_decision(self, current_board_state, current_block_state, cells, flag)

	def minimax_decision(self, current_board, current_block, actions, flag):
		for current_action in actions:
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_min_value = min_value(self, current_board_state, current_block_state, current_action, flag, 0)
			if current_action == actions[0] or current_min_value > best_value:
				best_action = current_action
				best_value = current_min_value
			update_lists(current_board_state, current_block_state, current_action, '-')

		return best_action


	def min_value(self, current_board_state, current_block_state, current_action, flag, depth):
		if terminal_test(self, current_board_state, current_block_state, depth) == True:
			return utility(self, current_board_state, current_block_state)

		blocks_allowed  = determine_blocks_allowed(current_action, current_block_state)
		actions = get_empty_out_of(current_board_state, blocks_allowed)

		for current_action in actions:
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_max_value = max_value(self, current_board_state, current_block_state, current_action, flag, depth + 1)
			if current_action == actions[0] or current_max_value < best_min_value:
				best_min_value = current_max_value
			update_lists(current_board_state, current_block_state, current_action, '-')

		return best_min_value

	def max_value(self, current_board_state, current_block_state, current_action, flag, depth):
		if terminal_test(self, current_board_state, current_block_state, depth) == True:
			return utility(self, current_board_state, current_block_state)

		blocks_allowed  = determine_blocks_allowed(current_action, current_block_state)
		actions = get_empty_out_of(current_board_state, blocks_allowed)

		for current_action in actions:
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_min_value = min_value(self, current_board_state, current_block_state, current_action, flag, depth + 1)
			if current_action == actions[0] or current_min_value > best_max_value:
				best_max_value = current_min_value
			update_lists(current_board_state, current_block_state, current_action, '-')

		return best_max_value

	def terminal_test(self, current_board_state, current_block_state, depth):
		if depth % 2 == 0 and depth >= 2:
			return True
		else:
			return False
		

	def utility(self, current_board_state, current_block_state):
		pass
