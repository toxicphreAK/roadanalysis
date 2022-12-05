import typer
import sqlite3
import re
from pathlib import Path
from typing import List
from .helper.printing import print_info, print_success

app = typer.Typer()

cur = sqlite3.Cursor

def get_num_elements(query: str):
    query_re = re.compile(r"SELECT ([\w\"'.]+,? ?)+ FROM .*")
    query_match = query_re.match(query)
    print(query)
    if query_match:
        print(len(query_match.groups()))


def run_query(cursor: sqlite3.Cursor, query: str) -> List[List[str]] | None:
    res = cursor.execute(query)
    results = res.fetchall()
    if results:
        return results
    return None


def print_results(level: int, name: str, results: List[List[str]]) -> None:
    """
    Prints the given results with an ident level
    """
    ident = "\t" * level
    print_success(f"{ident}{name}:")
    resultstring = ""
    for entry in results:
        for val in entry:
            resultstring += val
        print(ident, resultstring)


def get_groups(id: str):
    res = cur.execute(f'SELECT lnk_group_member_group."group" FROM lnk_group_member_group WHERE childGroup = "{id}";')
    group_memberships = res.fetchall()
    if group_memberships:
        print("\tGroup Memberships:")
        for group_membership in group_memberships:
            print("\t", group_membership[0])
            get_group_details(group_membership[0])


def get_group_details(id: str):
    res = cur.execute(f'SELECT displayName, description FROM Groups WHERE objectId = "{id}";')
    group = res.fetchone()
    if group:
        print("\t\t", group[0], group[1])


def get_approleassignments(id: str):
    res = cur.execute(f'SELECT resourceId FROM AppRoleAssignments WHERE principalId = "{id}";')
    app_role_assignments = res.fetchall()
    if app_role_assignments:
        print("\tApp Role Assignments:")
        for app_role_assignment in app_role_assignments:
            print("\t", app_role_assignment[0])
            get_serviceprincipals(app_role_assignment[0])


def get_serviceprincipals(id: str):
    res = cur.execute(f'SELECT appId FROM ServicePrincipals WHERE objectId = "{id}";')
    service_principals = res.fetchall()
    if service_principals:
        print("\t\tService Principals:")
        for service_principal in service_principals:
            print("\t\t", service_principal[0])
            get_applications(service_principal[0])


def get_applications(id: str):
    res = cur.execute(
        f'SELECT displayName, homepage, oauth2AllowIdTokenImplicitFlow, oauth2Permissions, publisherDomain FROM Applications WHERE appId = "{id}";')
    applications = res.fetchall()
    if applications:
        print("\t\t\tApplications:")
        for application in applications:
            print("\t\t\t", application[0], application[1], application[2], application[3], application[4])


"""for dynamic_rule in res.fetchall():
    # having index 0-3
    print(dynamic_rule[0], dynamic_rule[1], dynamic_rule[3])

    get_groups(dynamic_rule[1])
    get_approleassignments(dynamic_rule[1])"""


@app.command()
def get_membershiprules(
        database: Path = typer.Argument(
            "roadrecon.db",
            exists=True
        )
):
    print_info(f"Connecting to database file {database}")
    con = sqlite3.connect(database)
    cur = con.cursor()

    results = run_query(
        cur,
        "SELECT displayName, objectId, description, membershipRule \
        FROM Groups \
        WHERE membershipRule NOT NULL AND \
        membershipRuleProcessingState = 'On';"
    )
    print_results(1, "Membershiprules", results)
