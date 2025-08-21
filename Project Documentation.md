# Assessment Task 3 CT

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

### Analyse and Conclude

With the data I have gathered and researched, I've come to the conclusion that there is very little evidence supporting the idea that people from an area are more likely to have freinds from that area. Curiously enough, the specific goal I set out with has been the least interesting of the areas to analyse, with pretty similar results across the board, with areas echoing the entire school average. The other areas of investigation, added for additional interest, like whether or not people knew others going in were honestly more interesting. As an example of what I've seen, the average student at GHS comes from the Central Coast, knew people entering the school, and their friend group consists of 4 people from the central coast, 4 from the north, and 2 from the south. This pretty well matches up with where people come from, with the majority from the north and coast, with smaller numbers of those from the south. 

### PMI Chart for Oscar Coleman

| Plus | Minus | Implication |
|----- | ----- | ----------- |
| Simple, easy to understand GUI | Code is difficult to access | In general, the program is extremely advanced, the hosting outside of python was certainly an unexpected surprised, and makes for extremely easy browing. Most issues are simple and UX focused, with quick fixes available if really needed. Does an excellent job focusing on the UX. Graphs are interesting and easy to understand, even if some data appears to be missing. 
| Many, nuanced graphs | Confusing tabs (e.g. Canada tab without anything in it) | 
| Extremely easy to access (out of a python file) | Data lacking in certain points (e.g. no US data) |

### PMI Chart by Oscar Coleman

| Positives: | Negatives | Implications |
| ---------- | --------- | ------------ |
| Github repository is organised into clear and distinct folders. | The option within the UI to “view dataset” only allows a partial glimpse at the dataset due to display constraints inside the terminal. | On the whole, the user will be able to acquaint themselves with the research outcomes without difficulty or confusion.
| Code follows a smooth modular structure with functions carried over from  the data_function.py file to the main.py file functionally and effectively. | Use of the word “averages” within the UI is misleading as what is actually shown are the percentages. | “Averages” should be removed and replaced with “data” or “percentages.”
| UI works successfully and is easily understandable. |  |“View dataset” option could redirect to something such as a pop-up of the file in a separate window.|




### Evaluation

#### Requirement Outline

Comparative to my requirement outline, I figure my current product has been sucessful, not only is it capable of taking a large dataset, but its also bugless (to my knowledge), has an easy to navigate and SIMPLE user interface and has a variety of options for comparisons.

#### Peer Feedback

Peer feedback wise, I'm happy with where I stand, most of the negatives are agreeable and could probably have been fixed with further time. On the terms of the averages, the numbers displayed are the averages of all the responses as a percent, though this is 100% a mistake that could be made.

#### Project Management

I feel my project management was middling during this production, it's certainly not my worst managed project, but I also feel work could have gone more smoothly, the github commits are for the mostpart spread out, and the work was done pretty successfully over time, though the time I took to learn pandas and matplotlib was very close to the backend of the project's development period, making these elements quite late to be added comparative to choices and the theoretical elements.

#### Data + Security

I don't have any quarrels with the way my data has been collected and displayed and with the security of the data. Everything that was collected has been anonymised and even the signifying time signatures were removed before porting to a CSV and uploading the dataset to github. Of course, secruity is always going to be lax with a public repository, but any identifying marks have been removed, beyond the fact this file in particular mentions the school. The data is as accurate as I could make it with the constraints of google forms and responses from people within the school. An expanded response-base would have been useful, but outside restraints obviously limited the amount I was capable of interviewing. 