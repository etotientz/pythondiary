def merge(left,right):
	temp=[]
	i,j,k=0,0,0
	while(i<len(left) and j<len(right)):
		if left[i]<=right[j]:
			temp.append(left[i])
			i+=1
		else:
			temp.append(right[j])
			k+=(len(left)-i)
			j+=1
	temp+=left[i:]
	temp+=right[j:]
	return temp,k





def mergesort(a):
	if len(a)<=1:
		return a,0
	left,lcount=mergesort(a[:len(a)/2])
	right,rcount=mergesort(a[len(a)/2:])
	mid,mcount=merge(left,right)
	return mid,lcount+rcount+mcount



a=list(map(int,raw_input().split()))
print mergesort(a)