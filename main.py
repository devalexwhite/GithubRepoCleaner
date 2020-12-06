from github import Github
from rich.console import Console
from rich.table import Table

console = Console()

# Set your Github access token
console.print("Enter a Github access token that has the `delete_repo` permission", style="blue")
console.print ("(https://docs.github.com/en/free-pro-team/github/authenticating-to-github/creating-a-personal-access-token)")
token = console.input("\nAccess token: ")

g = Github(token)

  
def printRepos():
  allRepos = []
  repoTable = Table(title="Repos")
  repoTable.add_column("#")
  repoTable.add_column("Name")
  repoTable.add_column("URL")
  repoTable.add_column("Privacy")
  repoTable.add_column("Forked?")
  i = 0
  g.get_user().update()
  for repo in g.get_user().get_repos():
    allRepos.append(repo)
    i+=1

    repoTable.add_row(str(i), repo.name, repo.html_url, ("Private" if repo.private else "Public"), ("Yes" if repo.fork else "No"))
  console.print(repoTable)
  return allRepos

def repoDelete(allRepos):
  console.print("\n\nEnter a repo number to delete", style="blue")
  toDelete = console.input("\n#: ")
  
  repo = allRepos[(int(toDelete) - 1)]

  console.print("Delete ", repo.name, "?", style="blue")
  response = console.input("\n(Y/N): ")

  console.clear(True)
  if (response.lower() == "y"):
    try:
      repo.delete()
    except:
      console.print("\nAn error occurred while deleting the repository.", style="bold red")
      console.print("\n")
    else:
      console.print("\nREPO DELETED", style="bold red")
  else:
    console.print("\nDelete skipped", style="blue")



while 1:
  allRepos = printRepos()
  repoDelete(allRepos)
  