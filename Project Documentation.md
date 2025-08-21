# Assessment Task 3 CP

#### *Charles McDonagh*

### Hypothesis

People are more likely to make friends with people who live nearby to them then those further from them.

### Mind Map

![Mindmap](./images/mindmapp.png)

### Requirements Outline

Functional Requirements:

- The ability to load large sets of data and to be modular enough to be able to be moved to take different file types.
- The charts need to be clearly visible even to someone without any experience in the field.
- The user interface needs to be simple to navigate and load without issues.
- There shouldn't be any bugs in the display and processing of data

Nonfunctional Requirements: 

- The User Interface doesn't take away from user experience.
- No bugs are present within the non-vital parts of the UI (e.g. choices work where they are supposed to.)


### Use Case

*Actor:* User
*Goal:* To access and look through the dataset.

Preconditions:
The dataset is already downloaded
The interface is running and active.

Main Flow:

The user opens to see a GUI
User selects one of the following options:
a. View visualisation (e.g., chart or graph of selected data)
b. Search or filter data based on specific criteria

The system performs this action

Postconditions:

User has viewed and/or interacted with the data.

Data remains unchanged despite viewing.

### SEE-I Paragraph

Gosford High School is a school who's catchment area is larger then most, and this will obviously lead to differences in the ways groups function compared with a regular school. Friendgroups, though wide, through my interviews, often seem to have smaller subsets of people who live at least somewhat closeby to eachother, who are more capable of meeting up in real life outside of school hours. For example, if I had a friend group of 6 people, maybe 2 of them would also live in my area, and the other 3 in another, we would then be able to meet up in real life without too much travel time, and also have a large friend group at school. From what I've gathered its like having a smaller friendgroup within the larger one, with potential for inter-group meetings too.

### Data Dictionary

| Field | Datatype | Format for Display | Description | Example |Valdiation |
| -------- | -------| ------ | ----------- | ------- | --------  |
| Year Group | integer | N | Year group of the respondant | 9 | Will only be 10 or 9 due to the groups where the form was sent
| Region | Object | XX...XX | The location of th respondant | Central Coast | Any number of characters, just no numbers
| Year 7 First Day | Object | XX...XX | Did the respondant know people day 1 year 7 | Yes | Either Yes, No or Maybe
| Friend Group Size | Integer | N | Size of the respondant's friend group group | 7 | Between 1 and 10 |
| 10 Closest Friends | Integer | N | The number of friends of the respondant's friend group from each location, there will be 3 catagories, nearby, north or south | 2 From North, 6 From Around, 2 from South | All 3 together will add up to 10, will be numbers between 1-10

