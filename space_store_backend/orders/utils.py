import random
import string


def random_string_generator(char_size=3, num_size=6, chars=string.ascii_uppercase, nums=string.digits):
    temp_char = ''.join(random.choice(chars) for _ in range(char_size))
    temp_num = ''.join(random.choice(nums) for _ in range(num_size))
    return temp_char + temp_num


def unique_order_id_generator(instance):
    order_new_id = random_string_generator()

    Klass = instance.__class__

    qs_exists = Klass.objects.filter(order_id=order_new_id).exists()
    if qs_exists:
        return unique_order_id_generator(instance)
    return order_new_id
