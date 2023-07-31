from rich.console import Console
from rich.table import Table
from source import write_to_txt_file

def display_options(options, console):
    for index, option in enumerate(options, start=1):
        console.print(f"{index}. [cyan]{option}[/cyan]")

def get_user_choice(options, console):
    while True:
        try:
            choice = int(console.input("[bold]Enter the option number: [/bold]"))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                console.print("[bold red]Invalid option number. Please try again.[/bold red]")
        except ValueError:
            console.print("[bold red]Invalid input. Please enter a valid option number.[/bold red]")

def input_cli(console):
    stream_options=["BT-BS", "MT", "DoubleMajor", "dual", "dualB", "dualC", "Mdes", "MBA", "Phd", "Msc", "MSR"]
    console.print("\n[bold]Select your [cyan]stream[/cyan]:[/bold]\n")
    display_options(stream_options, console)
    selected_stream = get_user_choice(stream_options, console)
    console.print(f"\n[bold]Your selected stream: [blue_violet]{selected_stream}[/blue_violet][/bold]\n")
    

    branch_options=["AE", "BSBE", "CE", "CHE", "CSE", "EE", "ES", "ME", "MSE", "PHY", "CHM", "MTH", "ECO", "DES", "IME", "HSS"]
    console.print("[bold]Select your [cyan]branch[/cyan]:[/bold]\n")
    display_options(branch_options, console)
    selected_branch = get_user_choice(branch_options, console)
    console.print(f"\n[bold]Your selected branch: [blue_violet]{selected_branch}[/blue_violet][/bold]\n")
    
    folder_path = console.input("[bold yellow]Enter the path to the folder performas' folder: [/bold yellow]")
    return folder_path, selected_stream, selected_branch

def capitalize_words(name):
    words = name.split("-")
    words = [word.capitalize() for word in words]

    return " ".join(words)

def output_cli(dict, selected_stream, selected_branch, console):
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Company")
    table.add_column("Role")


    for company in dict[selected_stream][selected_branch]:
        company, role = company.split("_")

        company = capitalize_words(company)
        role = capitalize_words(role)

        table.add_row(
            company, role
        )
        # print(company + " --> " + role)
        # write_to_txt_file(str(company) + "\n")
    console.print(table)
    return

if __name__ == "__main__":
    console = Console()
    input_cli()
