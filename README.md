# Project-4-Backend

Description:
Lizt is an application for making, sharing, and organizing lists of anything. Users can make and edit their own lists, compile other users lists, search for lists by keyword and send a list as a text to anyone. Think of it as Pinterest but for lists.






```
Model for Post
 {
        title: String,
        summary: String,
        revisit: String,
        restID: [{
            type: mongoose.Schema.Types.ObjectId,
            ref: 'Restaurant'
        }]
    }
```
