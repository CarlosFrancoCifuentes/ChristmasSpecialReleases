class Game_Score:

    null = 0
    strike = 10
    last_num = 0

    def __init__ (self, score_card):
        self.score_card = list(score_card)

    @staticmethod
    def special_sum(special_cha):
        total_value = 0
        for cha in special_cha:
            if cha.isdigit():
                total_value += int(cha)
                Game_Score.last_num = int(cha)
            if cha == "-":
                Game_Score.last_num = 0
            if cha == "X":
                total_value += Game_Score.strike
            if cha == "/":
                total_value += (Game_Score.strike - int(Game_Score.last_num))
        return total_value

    def calculate_points(self):
        final_points = 0
        num_throw = 0
        num_frame = 0
        num_throw_frame = 0

        for pins in self.score_card:
            if num_frame == 9:
                final_points += Game_Score.special_sum(self.score_card[num_throw:])
                return final_points
            if pins.isdigit():
                final_points += int(pins)
                Game_Score.last_num = pins
                if num_throw_frame > 0:
                    num_throw_frame = 0
                    num_frame += 1
                else:
                    num_throw_frame += 1
                num_throw += 1
            if pins == "-":
                Game_Score.last_num = 0
                if num_throw_frame > 0:
                    num_throw_frame = 0
                    num_frame += 1
                else:
                    num_throw_frame += 1
                num_throw += 1
            if pins == "X":
                final_points += Game_Score.special_sum(self.score_card[num_throw: num_throw + 3])
                num_throw += 1
                num_frame += 1
            if pins == "/":
                final_points += Game_Score.special_sum(self.score_card[num_throw: num_throw + 2])
                num_throw += 1
                num_throw_frame = 0
                num_frame += 1