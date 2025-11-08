def print_mul_arg(*pramod_list):
    # args - List
    for i in pramod_list:
        print(i)

print_mul_arg(1,2,3,4)
print_mul_arg("pramod")
print_mul_arg("pramod","Rose","Love","Arti")
print_mul_arg("pramod","Rose","Love",3.14)
print_mul_arg("pramod","Rose","Love",3.14, True)