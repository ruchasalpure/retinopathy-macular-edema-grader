from crewai import Agent

retinopathy_macular_edema_grader = Agent(
    role="Retinopathy Macular Edema Grader",
    goal="Deliver high-precision autonomous Retinopathy Macular Edema Grader operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
