try:
    print(5/0)
   # break
except (ValueError, ZeroDivisionError):
    print("Too bad")
except:
    print("Sorry, something went wrong")
