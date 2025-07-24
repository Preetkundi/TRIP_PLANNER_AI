from crewai import Task
from crew.TravelAgents import planner_agent, guide_agent

planning_task = Task(
    description=(
        "Plan a personalized {days}-day itinerary for {destination}."
        " The user prefers a {budget} budget and is interested in {interests}."
        " Respond with a clear and detailed travel plan."
    ),
    expected_output="A day-wise itinerary with suggestions for places, experiences, and budgeting tips.",
    agent=planner_agent,
    async_execution=False,
    output_file="plan.txt",  # optional
    name="Trip Planning Task"
)

guide_task = Task(
    description=(
        "Using the trip plan, act as a travel guide and suggest local tips, safety advice, must-try foods, and hidden gems for {destination}."
        " The user is interested in {interests} and will travel for {days} days."
    ),
    expected_output="Final guide with local tips and travel suggestions.",
    agent=guide_agent,
    async_execution=False,
    output_file="guide.txt",  # optional
    name="Local Guide Task"
)
