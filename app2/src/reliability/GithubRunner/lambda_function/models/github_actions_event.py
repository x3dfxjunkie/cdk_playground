"""
    GithubActionsEvent Model, Entry point is GithubActionsEvent
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List

from dataclasses_json import DataClassJsonMixin


@dataclass
class WorkflowJob(DataClassJsonMixin):
    """
    Workflow Job Event from Github Action webshot
    """

    id: int
    run_id: int
    run_url: str
    run_attempt: int
    node_id: str
    head_sha: str
    url: str
    html_url: str
    status: str
    conclusion: Any
    started_at: str
    completed_at: Any
    name: str
    steps: List[Any]
    check_run_url: str
    labels: List[str]
    runner_id: int
    runner_name: str
    runner_group_id: int
    runner_group_name: str


@dataclass
class Owner(DataClassJsonMixin):
    """
    Owner Event from Github Action webshot
    """

    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


@dataclass
class Repository(DataClassJsonMixin):
    """
    Repository Event from Github Action webshot
    """

    id: int
    node_id: str
    name: str
    full_name: str
    private: bool
    owner: Owner
    html_url: str
    description: str
    fork: bool
    url: str
    forks_url: str
    keys_url: str
    collaborators_url: str
    teams_url: str
    hooks_url: str
    issue_events_url: str
    events_url: str
    assignees_url: str
    branches_url: str
    tags_url: str
    blobs_url: str
    git_tags_url: str
    git_refs_url: str
    trees_url: str
    statuses_url: str
    languages_url: str
    stargazers_url: str
    contributors_url: str
    subscribers_url: str
    subscription_url: str
    commits_url: str
    git_commits_url: str
    comments_url: str
    issue_comment_url: str
    contents_url: str
    compare_url: str
    merges_url: str
    archive_url: str
    downloads_url: str
    issues_url: str
    pulls_url: str
    milestones_url: str
    notifications_url: str
    labels_url: str
    releases_url: str
    deployments_url: str
    created_at: str
    updated_at: str
    pushed_at: str
    git_url: str
    ssh_url: str
    clone_url: str
    svn_url: str
    homepage: str
    size: int
    stargazers_count: int
    watchers_count: int
    language: str
    has_issues: bool
    has_projects: bool
    has_downloads: bool
    has_wiki: bool
    has_pages: bool
    forks_count: int
    mirror_url: Any
    archived: bool
    disabled: bool
    open_issues_count: int
    license: Any
    allow_forking: bool
    is_template: bool
    topics: List[Any]
    visibility: str
    forks: int
    open_issues: int
    watchers: int
    default_branch: str


@dataclass
class Organization(DataClassJsonMixin):
    """
    Organization Event from Github Action webshot
    """

    login: str
    id: int
    node_id: str
    url: str
    repos_url: str
    events_url: str
    hooks_url: str
    issues_url: str
    members_url: str
    public_members_url: str
    avatar_url: str
    description: str


@dataclass
class Enterprise(DataClassJsonMixin):
    """
    Enterprise Event from Github Action webshot
    """

    id: int
    slug: str
    name: str
    node_id: str
    avatar_url: str
    description: str
    website_url: str
    html_url: str
    created_at: str
    updated_at: str


@dataclass
class Sender(DataClassJsonMixin):
    """
    Sender Event from Github Action webshot
    """

    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


@dataclass
class GithubActionsEvent(DataClassJsonMixin):
    """
    Github Action Main Model Event from Github Action webshot
    """

    action: str
    workflow_job: WorkflowJob
    repository: Repository
    organization: Organization
    enterprise: Enterprise
    sender: Sender
