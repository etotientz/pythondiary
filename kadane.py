a=list(map(int,raw_input().split()))

current_max=0;
best_max=-9999999999
posit=0
for i,l in enumerate(a):
	if l<0:
		posit=-1
	if current_max+l>0:
		current_max=current_max+a[i]
	else:
		current_max=0
	if current_max>best_max:
		best_max=current_max
if posit==0:
  print best_max
else:
	print max(a)
