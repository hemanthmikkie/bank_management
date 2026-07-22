reg_user_id="Hemanth"
reg_user_pass=1234
def user_login(user_id,_pass):
    if user_id==reg_user_id and _pass==reg_user_pass:
        return True
    else:
        return False      
valid= user_login("Hemanth",1234)
def show_reels(is_lgin_):
    if is_lgin_==True:
        print("showing reels")
    else:
        print("please login to see reels")
show_reels(valid)