# is_logged_in = True

# def decorator (func) :
#     def wrapper (is_logged_in):
#         if is_logged_in :
#             func()
#         else :
#             print("Please login first")
#     return wrapper

# @decorator
# def greet ():
#     print("welcome to your profile")

# greet(is_logged_in)


# def auth_decorator (func) :
#     def wrapper(role , *args ,  **kwargs): 
#         if role.lower() == "admin":
#             func( *args ,  **kwargs)
#         else :
#             print("Access denied")

#     return wrapper

# # role = "user"

# @auth_decorator
# def auth():
#     print("access granted")

# auth("user")
# auth("admin")



