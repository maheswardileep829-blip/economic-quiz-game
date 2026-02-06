import random

print("=" * 50)
print("ECONOMICS QUIZ GAME")
print("=" * 50)

# Terms dictionary - ADD MORE AS YOU GO
terms = {
    "GDP": "Total value of all goods and services produced in a country",
    "Inflation": "General increase in prices and fall in purchasing value of money",
    "Supply": "Amount of a product available for sale",
    "Demand": "Desire for a product by consumers",
    "Monopoly": "When one company controls an entire market",
    "Recession": "Period of economic decline",
    "Interest Rate": "Cost of borrowing money",
    "Stock": "Share of ownership in a company",
    "Dividend": "Payment to shareholders from company profits",
    "Capital": "Money or assets used to start a business",
    "Opportunity Cost": "The loss of something when you choose to do something else",
    "Revenue": "The total amount of money a business earns before any expenses",
    "Profit": "The total amount of money a business earns after calculating expenses",
    "Asset": "A tangible resource that holds present or future economic value",
    "Liabilty": "An obligation to transfer economic resources to another party in the future",
    "Equity": "Fair and just distribution of resources, opportunities, and outcomes across society",
    "Market Economy": "An economic system where production and prices are determined by unrestricted competition between privately owned businesses",
    "Fiscal Policy": "The use of government spending and taxation to influence economic conditions",
    "Monetary Policy": "A country's central bank managing the money supply and interest rates to do what they want",
    "Unemployment Rate": "The percent of the workforce that is jobless, actively seeking employment, and available to work"
}

# Get number of questions
num_questions = min(int(input("\nHow many questions (max 15)? ")), len(terms))

# Pick random terms
terms_list = list(terms.items())  # This now gives (term_name, term_data) pairs
quiz_terms = random.sample(terms_list, num_questions)

score = 0
wrong_list = []

def create_multiple_choice(correct_term, correct_definition, all_terms):
    # Get 3 random wrong answers from OTHER terms
    other_terms = [t for t in all_terms if t != correct_term]
    wrong_terms = random.sample(other_terms, 3)
    
    # Get their definitions (they're just strings now!)
    wrong_definitions = [all_terms[t] for t in wrong_terms]  
    
    # Combine correct + wrong
    all_choices = [correct_definition] + wrong_definitions
    
    # Shuffle them
    random.shuffle(all_choices)
    
    # Find where correct answer ended up
    correct_position = all_choices.index(correct_definition) + 1
    
    return all_choices, correct_position

# Quiz loop
for i, (term, correct_definition) in enumerate(quiz_terms, 1):
    
    print(f"\n{'='*50}")
    print(f"QUESTION {i} of {num_questions}")
    print(f"{'='*50}")
    print(f"\nWhat is {term}?\n")
    
    # Create multiple choice
    choices, correct_position = create_multiple_choice(term, correct_definition, terms)
    
    # Display choices
    for j, choice in enumerate(choices, 1):
        print(f"{j}. {choice}")
    
    # Get user answer (1-4)
    user_answer = int(input("\nYour answer (1-4): "))
    
    # Check if correct
    if user_answer == correct_position:
        print("✓ CORRECT! 🔥")
        score += 1
    else:
        print(f"✗ WRONG!")
        print(f"Correct answer: {correct_definition}")
        wrong_list.append(term)
    
    input("\nPress Enter to continue...")


# Results
print("\n" + "=" * 50)
print("FINAL RESULTS")
print("=" * 50)
print(f"Score: {score}/{num_questions}")
percentage = (score / num_questions) * 100
print(f"Percentage: {round(percentage, 1)}%")

if percentage >= 90:
    print("🔥 EXCELLENT! You're ready for DECA!")
elif percentage >= 70:
    print("💪 Good job! Study these terms more:")
else:
    print("📚 Keep studying! Focus on:")

if wrong_list:
    print("\nTerms to review:")
    for term in wrong_list:

        print(f"  - {term}")
