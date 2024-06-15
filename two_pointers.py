import streamlit as st 

st.title("Two pointer algo")
nums=st.text_input("give list of numbers with ,")#1,5354
if nums:
    nums=nums.split(",")
    nums=list(map(int,nums))

target=st.text_input("Enter the target")
if target:
    target=int(target)

dlist=nums
dlist=sorted(dlist)

left=0
right=len(nums)-1
while left<right:
    curr=dlist[left]+dlist[right]
    st.info(f"The sum left and right index value is {curr}")
    if target==curr:
        st.info(f"The current value adds to make the target {target}")
        if dlist[left]==dlist[right]:
            findex=nums.index(dlist[left])
            sindex=nums[findex+1:].index(dlist[right])+findex+1
            st.success([findex,sindex])
            break
        st.success(sorted([nums.index(dlist[left]),nums.index(dlist[right])]))
        break
    elif curr<target:
        st.write(f"The Sum of values {dlist[left]} and {dlist[right]} is less than {target}")
        left+=1
    else:
        st.write(f"The Sum of values {dlist[left]} and {dlist[right]} is greater than {target}")
        right-=1
