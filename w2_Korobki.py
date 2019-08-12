ox1 = int(input())
oy1 = int(input())
oz1 = int(input())
ox2 = int(input())
oy2 = int(input())
oz2 = int(input())
# variant1
oxv1 = (ox1 - ox1 % ox2) / ox2
oyv1 = (oy1 - oy1 % oy2) / oy2
ozv1 = (oz1 - oz1 % oz2) / oz2
var1 = oxv1 * oyv1 * ozv1
# variant2
oxv2 = (ox1 - ox1 % oy2) / oy2
oyv2 = (oy1 - oy1 % oz2) / oz2
ozv2 = (oz1 - oz1 % ox2) / ox2
var2 = oxv2 * oyv2 * ozv2
# variant3
oxv3 = (ox1 - ox1 % oy2) / oy2
oyv3 = (oy1 - oy1 % ox2) / ox2
ozv3 = (oz1 - oz1 % oz2) / oz2
var3 = oxv3 * oyv3 * ozv3
# variant4
oxv4 = (ox1 - ox1 % oz2) / oz2
oyv4 = (oy1 - oy1 % ox2) / ox2
ozv4 = (oz1 - oz1 % oy2) / oy2
var4 = oxv4 * oyv4 * ozv4
# variant5
oxv5 = (ox1 - ox1 % ox2) / ox2
oyv5 = (oy1 - oy1 % oz2) / oz2
ozv5 = (oz1 - oz1 % oy2) / oy2
var5 = oxv5 * oyv5 * ozv5
# variant6
oxv6 = (ox1 - ox1 % oz2) / oz2
oyv6 = (oy1 - oy1 % oy2) / oy2
ozv6 = (oz1 - oz1 % ox2) / ox2
var6 = oxv6 * oyv6 * ozv6
print(int(max(var1, var2, var3, var4, var5, var6)))
