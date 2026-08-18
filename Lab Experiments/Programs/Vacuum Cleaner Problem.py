def reflex_vacuum_agent(location, status):
    if status == 'Dirty':
        return 'Suck'
    elif location == 'A':
        return 'Right'
    elif location == 'B':
        return 'Left'

def run_simulation(initial_location, status_A, status_B):
    # Environment dictionary representation
    env = {'A': status_A, 'B': status_B}
    location = initial_location
    
    print(f"Initial State -> Location: {location} | Room A: {env['A']} | Room B: {env['B']}\n")
    
    steps = 0
    # Run loop until both rooms are Clean
    while env['A'] == 'Dirty' or env['B'] == 'Dirty' or steps < 2:
        status = env[location]
        action = reflex_vacuum_agent(location, status)
        
        print(f"Location: {location} | Status: {status} -> Action Chosen: {action}")
        
        if action == 'Suck':
            env[location] = 'Clean'
            print(f"--- Cleaned Room {location} ---")
        elif action == 'Right':
            location = 'B'
        elif action == 'Left':
            location = 'A'
            
        steps += 1
        if env['A'] == 'Clean' and env['B'] == 'Clean':
            break

    print(f"\nFinal State -> Room A: {env['A']} | Room B: {env['B']}")
    print("Environment is fully cleaned!")

# Scenario: Agent starts in Room A, Room A is Dirty, Room B is Dirty
run_simulation(initial_location='A', status_A='Dirty', status_B='Dirty')