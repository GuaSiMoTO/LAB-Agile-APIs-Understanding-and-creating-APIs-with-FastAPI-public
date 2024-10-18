
![](https://user-images.githubusercontent.com/970858/63474771-d6734700-c469-11e9-83bb-9429da563909.png)

# LAB-Agile-APIs-with-FastAPi-and-MongoDB-Understanding-and-creating-APIs-with-FastAPI

## Introduction

We've only learned the basics of API communication today, but what can we do with an API? We hope you are ready to get your mind blown!

We are going to work just with postman to send petitions to [The Cocktail DB](https://www.thecocktaildb.com/)

## Requirements

- [Learn how to fork this repo](https://guides.github.com/activities/forking/)
- Clone this repo into your `code/labs` folder
- Paste the screen of the activities on this file. (remember to upload images).
- Answer all the questions done on this file (take pictures when needed).
- Use postman to retrieve/send the data.

## Questions

1. **What is an API?**
1. **What does any API respond if you send something wrong on a request?** (take a picture with postman on one api you have chosen)
1. **Which HTTP verb is used for updating data?**
1. **Which HTTP verb is used for deleting data?**
1. **What does SOLID mean and why it's useful?** (go a bit deeper reasearching!)

## Moe's Tavern API: Cocktail Missions


<img src="https://github.com/user-attachments/assets/adc9ff8a-4393-4fbf-885f-0adb903018ea" height="400" width="800" align="center">

---

Listen up, folks! Moe here, from Moe's Tavern! Today, you're not just gonna order cheap beers and hang around the bar like Barney, no sir. We're gonna get some real work done. Turns out, the world of APIs isn’t just for computer nerds, it’s also for bringing me recipes for fancy cocktails. And guess what… you’re the ones who are gonna do all the work!

You're going to use Postman to make requests to The Cocktail DB API, just like you're taking orders for my tavern. But don’t get it wrong! Every mission is a special order, and I don’t want you messing it up. If you do it right, maybe I’ll let you try something that’s not just a Duff.


### Mission 1: The Special Customer Order
- I’ve got a weird customer who only wants drinks with **milk**. So go ahead and bring me **all the drinks** that have `milk` as an ingredient. No idea who orders that in a bar, but you do the job.


### Mission 2: The Mysterious Orange
- Another customer’s asking for something with **orange**. I need you to get **all drinks made with orange**. And once you have it, show me a **preview of the first cocktail** you find. You know, just to see if this orange stuff is any good.

### Mission 3: Make It Bigger!
- That orange drink caught my eye! But now I need a **medium-sized preview**. Yeah, no thumbnails, I want to see it properly! Don’t make me mad.

### Mission 4: The Mystery Customer
- I’ve got an order with ID **13938**. No clue what it is, but I need you to find out what drink corresponds to that ID. And make it snappy!

### Mission 5: Drinker’s Luck
- I’m bored of the same old drinks, so surprise me with a **random cocktail**. Sometimes, you don’t know what you need until you see it on the bar.

### Mission 6: We Need Variety!
- Not everything can be Duff beer. I want to see **all the cocktail categories** you can offer me. This bar needs options, dammit!

---

# PokeIteration: Pokémon API with FastAPI



Did you think the lab was over? The best part has just begun !!!! 

In this exercise, we will immerse ourselves in the exciting world of **Pokémon** by using **FastAPI** to create an interactive API that allows users to become Pokémon Trainers. Each of you will develop various endpoints to interact with a list of initial Pokémon, capture new ones, manage your team, and evolve them.

Additionally, each endpoint should be accompanied by a **Pydantic model** to handle validations and clear responses indicating whether the request was successful or if an error occurred. Errors must be handled with descriptive messages explaining what went wrong. Don’t worry, Pydantic will handle 50% of the work with validations!



### Exercise 1: **Add Favorite Initial Pokémon**
**Create a list of favorite initial Pokémon**:

<img src="https://github.com/user-attachments/assets/0da3f010-c0cf-468a-b984-b4e6635e67f1" height="350" width="350" align="right">

   - We need a list of initial Pokémon. Create a variable where you will store your favorite initial Pokémon.
   - Develop an endpoint that allows **adding** Pokémon to this list.
   - The Pokémon format should be as follows:
     ```json
     {
       "id": 1,
       "name": "Bulbasaur",
       "type": "Grass",
       "level": 5
     }
     ```
   - **Validation**: Ensure that there are no duplicates based on the Pokémon's `id`.
   - **Error Handling**: If you try to add a Pokémon with the same `id`, return an error indicating that the Pokémon already exists in the list.


<img src="https://github.com/user-attachments/assets/097d4c6e-2986-425e-b7a8-51966e550cd8" height="700" width="350" align="right">

### Exercise 2: **Show All Initial Pokémon**
**Create an endpoint to list all initial Pokémon**:
   - This endpoint should return the complete list of initial Pokémon that you have added.
   - **Response**: If there are no Pokémon in the list, return a message indicating that the list is empty.

### Exercise 3: **Show a Specific Pokémon**
**Create an endpoint to display a Pokémon by its `id`**:
   - The endpoint should receive an `id` as a parameter and return the corresponding Pokémon's information.
   - **Error Handling**: If the `id` does not exist, return an error specifying that the Pokémon was not found.

### Exercise 4: **Filter Pokémon by Type or Level**
**List Pokémon filtered by type or level**:
   - Create an endpoint that allows filtering the list of initial Pokémon using **query parameters** to search by type (`type`) or level (`level`).
   - **Validation**: If the parameters don't match any Pokémon, return a message indicating that no matches were found.

### Exercise 5: **Assign an Initial Pokémon to Your Team**

**Create an endpoint to assign a random initial Pokémon to your team**:
   - This endpoint will select a **random** Pokémon from the list of initials and assign it to a new variable representing your Pokémon team.
     <img src="https://github.com/user-attachments/assets/318e151a-21a5-4e16-a5ae-dda751002f7a" height="700" width="350" align="right">
   - **Validations**: 
     - Check if there is already a Pokémon in your team. If so, decide whether to remove it (only if it is an initial Pokémon) or return an error.
     - If removing, ensure that only initial Pokémon are removed. If it's not an initial Pokémon, protect your team so you don't lose Pokémon captured later on.
   - **Error Handling**: If you try to add a new initial Pokémon without releasing the current one, return an error indicating that you already have an assigned initial Pokémon.
     
### Exercise 6: **Update Pokémon Information**
 **Create an endpoint to update a Pokémon's data**:
   - This endpoint will allow modifying the Pokémon's properties, such as name or level.
   - **Validation**: Verify that the Pokémon's `id` exists before updating its data.
   - **Error Handling**: If the Pokémon does not exist, return an appropriate error.


### Exercise 7: **Delete a Pokémon from the Initial List**
**Create an endpoint to delete a Pokémon from the initial list**:
   - This endpoint will receive the Pokémon's `id` and remove it from the list.
   - **Error Handling**: If the Pokémon is not in the list, return an error indicating that it was not found.

### Exercise 8: **Release a Pokémon from the Team**
**Create an endpoint to release a Pokémon from your team**:
   - This endpoint will allow you to release a Pokémon from your team if you no longer want it.
   - **Validation**: Ensure that the team has a Pokémon before attempting to release it.
   - **Error Handling**: If you try to release a Pokémon when the team is empty, return an error.

---

## Bonus

- Find one API where you can limit the pages of reponse by yourself and explain how it works.
- Yes... Of course it can't be thecocktaildb.com, you can try [ProgrammableWeb Directory](https://rapidapi.com/collection/list-of-free-apis) for example

## PokeBonus 1 **Evolve a Pokémon**
**Create an endpoint to evolve a Pokémon**:
   - This endpoint will allow a Pokémon to **evolve** under certain conditions, for example, after reaching a specific level.
   - **Validations**: 
     - Verify that the Pokémon meets the level requirements to evolve.
     - Change the Pokémon's name and type after evolution.
   - **Error Handling**: If the Pokémon does not meet the conditions to evolve, return an error specifying why.

## PokeBonus 2 **Capture New Pokémon**
**Capture a new Pokémon from different routes**:
   - Create two lists of Pokémon, one for the **Kanto route** and another for the **Sinnoh route**.
   - Create an endpoint that receives the route name as a parameter and captures a random Pokémon from the corresponding list.
   - **Validation**: Ensure that the captured Pokémon can be added to the team without replacing the initial ones.
   - **Error Handling**: If you try to capture a Pokémon without space in your team (or with some restriction), return an error explaining why the capture cannot proceed.

<img src="https://github.com/user-attachments/assets/ad9e87d5-2b79-4fa3-916c-87aecef1b5a6" height="400" width="800">

## Submission

Upon completion, run the following commands:
```
$ git add .
$ git commit -m "done"
$ git push origin main
```

Then create a Pull Request!!

## Extra Resources

- [JSON](https://www.json.org/)
- [POSTMAN](https://learning.getpostman.com/docs/postman/sending_api_requests/requests/)


![happy_coding](https://user-images.githubusercontent.com/970858/63899010-c23fc480-c9ea-11e9-84a2-542907e42362.png)
