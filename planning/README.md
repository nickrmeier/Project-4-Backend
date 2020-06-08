# Lizt - Proposal

Description:
Lizt is an application for making, sharing, and organizing lists of anything. Users can make and edit their own lists, compile other users lists, search for lists by keyword and send a list as a text to anyone. Think of it as Pinterest but for lists.


# Lizt - User Stories

![alt text](https://github.com/nickrmeier/Project-4-Backend/blob/master/images/IMG_2525.jpg?raw=true)

1. As a user I want ot be able to make lists easily available so I don't loose them. I want all of my lists to live in one place. I want to be able to text these lists, since texting is my preferred form of communication. 

2. As a user I want to customize my lists, and view/save other users lists for new ideas. I want to be able to search for lists around a certain subject for new ideas. I want to look back on my old lists for ideas, and to edit.


# Lizt - Routes

![alt text](https://github.com/nickrmeier/Project-4-Backend/blob/master/images/IMG_2532.jpg?raw=true)

# Lizt - Models
```

class Lizt(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Item(models.Model):
    lizt = models.ForeignKey(List, on_delete=models.CASCADE, related_name='item')
    lizt_item = models.CharField(max_length=100, default='no items')
    quantity = models.CharField(max_length=10, default='0')
    def __str__(self):
        return self.lizt_item

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    def __str__(self):
        """Return string representation of the user"""
        return self.email
        
```

# Lizt - Wireframes

![alt text](https://github.com/nickrmeier/Project-4-Backend/blob/master/images/wireframe-1.png?raw=true)

![alt text](https://github.com/nickrmeier/Project-4-Backend/blob/master/images/wireframe-2.png?raw=true)

![alt text](https://github.com/nickrmeier/Project-4-Backend/blob/master/images/wireframe-3.png?raw=true)



# Lizt - MPV

- Authentification
- Full CRUD
- Texting via Twilio (https://www.twilio.com/sms)

# Lizt - Gold Version

- Search function by keywords
- Autoformatting of lists items
