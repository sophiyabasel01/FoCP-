import sys
print("""
        Stop! Who would cross the Bridge of Death
        Must answer me these questions three, 'ere the other side he see.
        """
      )


def get_first_answer():
    first_answer_value = input("What is your name?")
    if len(first_answer_value.strip()) == 0:  # !caution: assuming any valid value as valid name (even number for now)
        return False
    return first_answer_value


# first question
first_answer = False
while not first_answer:
    first_answer = get_first_answer()
    if not first_answer:
        print('Must enter valid a name')

is_king = first_answer and first_answer.lower() == 'arthur'
if is_king:
    print("My liege! You may pass!")
    sys.exit(0)

# second question case
second_answer = input("What is your quest?")
if "grail" not in second_answer.lower():
    print("Only those who seek the Grail may pass.")
    sys.exit(0)

# third answer
third_answer = input("What is your favourite colour?")
if third_answer[0].lower() == first_answer[0].lower():
    print('You may pass!')
else:
    print('You must now face the Gorge of Eternal Peril.')
