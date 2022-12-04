with open("input.txt") as f:
    elf_payloads = []
    elf_carry = []
    for line in f:
        amount = line.replace("\n", "")  # remove newline
        if len(amount) == 0:
            elf_payloads.append(elf_carry)
            elf_carry = []
        else:
            elf_carry.append(int(amount))

    sum_elf_payloads = []
    for payload in elf_payloads:
        payload_sum = sum(payload)
        sum_elf_payloads.append(payload_sum)
    sorted_sums = sorted(sum_elf_payloads, reverse=True)
    print(sum(sorted_sums[:3]))
