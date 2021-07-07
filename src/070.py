result = 0
result2 = 0
vcf = "070.vcf"
# with open(vcf, 'r') as handle:
#     for line in handle:
#         if line.startswith("#"):
#             continue
#         result += 1
# print(result)

# with open(vcf, 'r') as handle:
#     for line in handle:
#         if line.startswith("##"):
#             continue
#         data = line.strip().split("\t")
#         result += 1
#         if data[6] == "PASS":
#             result2 += 1

# print(result)
# print(result2)
# print(result2/result)


with open(vcf, 'r') as handle:
    for line in handle:
        if line.startswith("##"):
            continue
        elif line.startswith("#"):
            header = line.strip().split("\t")
            filter_idx = header.index("FILTER")
            continue
        data = line.strip().split("\t")
        result += 1
        if data[6] == "PASS":
            result2 += 1

print(result)
print(result2)
print(result2/result)