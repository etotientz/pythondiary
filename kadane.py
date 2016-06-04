a=list(map(int,raw_input().split()))
start=end=start1=0
k=current_max=best_max=0
for i,l in enumerate(a):
	if max(a)<0:
		k=1
	if current_max+l>0:
		current_max+=a[i]
	else:
		current_max=0
		start=i+1
	if current_max>best_max:
		best_max=current_max
		start1,end=start,i+1
if k==0:
  print best_max,start1,end-1
else:
	print max(a)
