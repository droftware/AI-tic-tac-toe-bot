class Player64:

	def __init__(self):
		self.depth = 0
		pass

	def move(self,temp_board,temp_block,old_move,flag):
		#List of permitted blocks, based on old move.
		blocks_allowed  = determine_blocks_allowed(old_move, temp_block)
		#Get list of empty valid cells
		cells = get_empty_out_of(temp_board, blocks_allowed)

		return minimax_decision(self, temp_board, temp_block, cells, flag)

	def minimax_decision(self, temp_board, temp_block, actions, flag):
		board_state = temp_board[:]
		block_state = temp_block[:]
		for current_action in actions:
			current_board_state = board_state[:]
			current_block_state = block_state[:]
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_min_value = min_value(self, current_board_state, current_block_state, current_action, flag)
			if current_action == actions[0] or current_min_value > best_value:
				best_action = current_action
				best_value = current_min_value

		return best_action

	def min_value(self, temp_board_state, temp_block_state, temp_action, flag):
		if terminal_test(self, temp_board_state, temp_block_state) == True:
			return utility(self, temp_board_state, temp_block_state)

		blocks_allowed  = determine_blocks_allowed(temp_action, temp_block_state)
		actions = get_empty_out_of(temp_board_state, blocks_allowed)

		for current_action in actions:
			current_board_state = temp_board_state[:]
			current_block_state = temp_block_state[:]
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_max_value = max_value(self, current_board_state, current_block_state, current_action, flag)
			if current_action == actions[0] or current_max_value < best_min_value:
				best_min_value = current_max_value

		return best_min_value

	def max_value(self, temp_board_state, temp_block_state, temp_action, flag):
		if terminal_test(self, temp_board_state, temp_block_state) == True:
			return utility(self, temp_board_state, temp_block_state)

		blocks_allowed  = determine_blocks_allowed(temp_action, temp_block_state)
		actions = get_empty_out_of(temp_board_state, blocks_allowed)

		for current_action in actions:
			current_board_state = temp_board_state[:]
			current_block_state = temp_block_state[:]
			update_lists(current_board_state, current_block_state, current_action, flag)
			current_min_value = min_value(self, current_board_state, current_block_state, current_action, flag)
			if current_action == actions[0] or current_min_value > best_max_value:
				best_max_value = current_min_value

		return best_max_value
