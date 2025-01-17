import pandas as pd

# Sample data
data = {
    "Tip": [
        "Drink a large glass of water 10 minutes before your meal to feel less hungry.",
        "Keep meat, chicken, turkey and fish portions to about 3 ounces.",
        "Share one dessert.",
        "Use teaspoons, salad forks, or child-size forks, spoons, and knives to help you take smaller bites and eat less.",
        "Make less food look like more by serving your meal on a salad or breakfast plate.",
        "Eat slowly. It takes 20 minutes for your stomach to send a signal to your brain that you are full.",
        "Listen to music while you eat instead of watching TV (people tend to eat more while watching TV).",
        "Turn up the music and jam while doing household chores.",
        "Work out with a video that shows you how to get active.",
        "Deliver a message in person to a co-worker instead of sending an e-mail.",
        "Walking is one of the best ways to increase your activity level. Start slowly by walking five minutes more each day. Build up to 30 minutes, 5 days a week.",
        "Show your kids the dances you used to do when you were their age.",
        "Take the stairs to your office. Or take the stairs as far as you can, and then take the elevator the rest of the way.",
        "Catch up with friends during a walk instead of by phone.",
        "March in place while you watch TV.",
        "Choose a place to walk that is safe, such as your local mall.",
        "Park in a spot towards the back of the parking lot so you have to walk farther to get to the store.",
        "Get off the bus one stop early and walk the rest of the way home or to work if it is safe.",
        "Use TV breaks to stretch, take a quick walk around your home, or do some sit-ups.",
        "Do something active that you enjoy every day – shoot hoops, take a bike ride, garden, or line dance.",
        "Take a walk during your lunch break.",
        "Buy a mix of vegetables when you go food shopping.",
        "Choose veggie toppings like spinach, broccoli, and peppers for your pizza.",
        "Try eating foods from other countries. Many of these dishes have more vegetables, whole grains, and beans.",
        "Buy frozen and low-salt (sodium) canned vegetables if you are on a budget. They may cost less and keep longer than fresh ones.",
        "Do not skip meals. Eat breakfast, lunch, and dinner plus a snack. You will have a ready supply of energy and not get too hungry.",
        "Avoid getting too hungry by eating a healthy snack between meals.",
        "Eat a variety of colorful fruits and vegetables every day.",
        "Serve your favorite vegetable and a salad with low-fat macaroni and cheese.",
        "Stir fry, boil, or bake with non-stick spray or low-salt broth. Cook with less oil and butter.",
        "Try not to snack while cooking or cleaning the kitchen.",
        "Cook with smaller amounts of cured meats (jerky, smoked turkey and turkey bacon). They are higher in salt.",
        "Cook with a mix of spices instead of salt to add flavor.",
        "Try different recipes for baking or broiling meat, chicken, and fish.",
        "Choose foods with little or no added sugars to reduce calories.",
        "Choose brown rice instead of white rice.",
        "Have a big vegetable salad with low-calorie salad dressing when eating out.",
        "Share your main dish with a friend or have half wrapped to go before you start eating.",
        "Make healthy choices at fast food restaurants. Try grilled chicken instead of a cheeseburger.",
        "Skip the fries and chips and choose a side salad instead.",
        "Order fruit for dessert instead of ice cream or cake.",
        "Find a water bottle you really like and drink water from it every day.",
        "Eat a piece of whole, fresh fruit instead of drinking juice.",
        "If you drink whole milk, try changing to 2% milk, which has less fat. Once you get used to 2% milk, try 1% or fat-free (skim) milk. This will help you reduce the amount of fat and calories you take in each day.",
        "Drink water or seltzer instead of juice and regular soda.",
        "Eat foods made from whole grains, such as whole wheat bread, brown rice, oats, and whole grain corn.",
        "Use whole grain bread for toast and sandwiches.",
        "Keep a healthy snack with you, such as fresh fruit, a handful of nuts, and whole grain crackers.",
        "Slow down at snack time. Eating a bag of low-fat popcorn takes longer than eating a candy bar.",
        "Share a bowl of fruit with family and friends.",
        "Eat a healthy snack or meal before shopping for food. Do not shop on an empty stomach.",
        "Cook ahead and freeze food portions. This will help you have healthy and easy meals on days when you are too busy to cook.",
        "Shop at your local farmers market for fresh, local food.",
        "Make a list of food you need to buy before you go to the store.",
        "Keep a written record of what you eat for a week. It can help you see when you tend to overeat or eat foods high in fat or calories.",
        "Compare food labels on packages.",
        "Use calorie labeling information at fast food restaurants and on restaurant menus.",
        "Choose foods lower in saturated fats, trans fats, cholesterol, calories, salt, and added sugars.",
        "Try one new healthy food a week.",
        "Find ways to relax. Try deep breathing, taking a walk, yoga, or listening to your favorite music.",
        "Pamper yourself. Read a book, take a long bath, or meditate.",
        "Think before you eat. Try not to eat when you are bored, upset, or unhappy.",
        "Start by making small changes. Try to add one new change a week.",
        "Don’t get discouraged if you have a bad day. If you get off track, start again and keep at it.",
        "You don’t have to prevent diabetes alone. Ask your friends and family to help you out, and involve them in your activities.",
        "Consider registering for a diabetes prevention program in your area to help you make healthy lifestyle choices.",
    ],
    "Category": [
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Reduce portion sizes",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Be physically active",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Make healthy food choices",
        "Stress reduction/ mental health",
        "Stress reduction/ mental health",
        "Stress reduction/ mental health",
        "Stress reduction/ mental health",
        "Stress reduction/ mental health",
        "Stress reduction/ mental health",
        "Prevention programs",
    ]
}

# Count the number of tips and categories
num_tips = len(data["Tip"])
num_categories = len(data["Category"])

print(f"Number of tips: {num_tips}")
print(f"Number of categories: {num_categories}")

# Adjust the lists to match the length if necessary
if num_tips > num_categories:
    data["Tip"] = data["Tip"][:num_categories]  # Keep only the first n tips to match category count

# Now both lists should have the same length
df_tips = pd.DataFrame(data)

# Save the DataFrame to a new CSV file
df_tips.to_csv('tips_and_categories.csv', index=False)
print("Data saved to 'tips_and_categories.csv'")
