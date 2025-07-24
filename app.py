from flask import Flask, render_template, request
from crewai import Crew
from crew.TravelAgents import planner_agent, guide_agent
from crew.TravelTasks import planning_task, guide_task

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        destination = request.form.get('destination', '').strip()
        budget = request.form.get('budget', 'moderate').strip()
        days = request.form.get('days', '').strip()
        interests = request.form.get('interests', '').strip()

        if not destination or not days or not interests:
            return render_template('index.html', error="⚠️ Please fill in all required fields.")

        try:
            # Inject dynamic values
            for task in [planning_task, guide_task]:
                task.description = task.description.format(
                    destination=destination,
                    budget=budget,
                    days=days,
                    interests=interests,
                )

            crew = Crew(
                agents=[planner_agent, guide_agent],
                tasks=[planning_task, guide_task],
                verbose=True,
            )
            result = crew.kickoff()

            # ✅ Extract output from last task
            final_output = str(result)
            if final_output.lower().startswith("thought:"):
                final_output = "⚠️ Looks like the agent did not return an actual trip plan. Check the tasks or agent outputs."

            return render_template('result.html', result=final_output, destination=destination)

        except Exception as e:
            print("Error:", e)
            return render_template('result.html', result="❌ Something went wrong.")

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
