![Alt text](images/openroad_banner_01.png)

# OpenRoad

OpenRoad helps decide what comes next!

## Overview

OpenRoad is a roadmap coordination tool for OpenSpec projects.

Cunrently it is built to use with OpenCode but this will expand in the near future

It helps you turn a project roadmap into ordered, OpenSpec-friendly changes, so you can work above the level of individual change folders without losing control of implementation detail.

OpenSpec handles the changes. OpenRoad helps decide what comes next → Order is important!

```text
Roadmap
   ↓
Ordered OpenSpec changes
   ↓
Implementation
   ↓
Review
   ↓
Next roadmap item
```

## Yeah But Why???

OpenSpec is excellent for managing individual changes, but larger projects need a layer above each change: a place to track direction, sequencing, dependencies, and progress.

OpenRoad provides that layer.

The goal is to keep the roadmap visible while still allowing each change to remain observable, reviewable, and implementation-ready through OpenSpec.

We still want to review each OpenSpec change, but we need to coordinate the order, understand what's next and what's been done.

Some changes in any project, will inevitably rely on other changes having been done. We need a tool to coordinate this.

## Getting Started

### Installation

If you're reading this you are early! Very early! OpenRoad is currently in early public preview.

For now, the recommended way to try it is to clone the repository and install it locally with `uv`.

#### 0. Make sure GIT is installed!

You should have Git on your system - Please check this with `git --version`
If you don't then absolutely you need to that first - You are better off using a guide on how to this for your system

#### 1. Install UV

If you have UV installed check which version with: `uv --version`. The `0.10.10` version was used to develop this tool. So will likely work with the version specified or later.

Check [`uv docs`](https://docs.astral.sh/uv/) for installation and getting started with UV.

For maOS and Linux you can usually use:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
or
```bash
wget -qO- https://astral.sh/uv/install.sh | sh
```

On Windows using Powershell usually the following works:
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

But please refer to the UV documentation for the up to date installation method for your system

#### 2. Clone this repo (Clone OpenRoad repo)

clone this repo to a directory you'd want it to live for example if I like my repos on my D: drive on Windows I'd use my terminal to navigate to this directory

```bash
cd "D:/repos"
```
and clone the repo there with

```bash
git clone https://github.com/fixyCat/OpenRoad.git
```

#### 3. Install OpenRoad using UV

Once you've clone the repo navigate to it, so following the example above I'd navigate using

```bash
cd "D:/repos/OpenRoad"
```

Once in that directory install the tool using the command

```bash
uv tool install .
```
IMPORTANT remember to include the dot . as that specifies install the files in THIS folder

To reinstall the tool after an update or changes you would use the --reinstall flag

```bash
uv tool install --reinstall .
```

Check you've successfully installed OpenRoad with the command:

```bash
openroad --help
```

if you get the help menu for OpenRoad the tool is now installed!

### Using OpenRoad

So it is expected that you already have OpenSpec and OpenCode installed on your system, you actually do not need to have ran the command `openspec init` to use OpenRoad but it's best that you do run it first.

OpenRoad is built to be used with OpenCode and thus running `openspec init` please select OpenCode as your LLM/Agent

Once you have the above you can start using OpenRoad with the command:
```bash
openroad init
```

This will copy across the necessary files to the curent repo, for now please be careful using OpenRoad on existing repos, if there is no AGENTS.md already in the repo, things will likely be okay but please be careful overwriting your existing files. This will be better handled in upcoming releases

Checking the status i.e. have all the files copied across successfully with OpenRoad can also be done using the command:

```bash
openroad status
```

This will output a table showing you the status of whether the necessary files for the OpenRoad tool exist in the current repo. It's best to run this command from the repo root!

#### OpenRoad In Action!

So now that you've got OpenRoad intialized in your repo you are ready to create your first roadmap.md (located ./openroad/roadmap.md)

The structure is as follows:

```text
# Project Overview

< An Overview of the idea behind what you are trying to build >

## Goal

< Either the final deliverable or set of outcomes (For example several sets of tools as a suite) > 

### Additional Information

< Additional but noteworthy data/information >

---

# Phase 1

< Give an overview of what this phase is building and the overall expected outcome (for example early phases might need an MVP later phases refinements) >

## Milestone 1

< All about the deliverable what tangible work will count as progress - e.g. have the app doing x by the end of the milestone >

## Items

id: 
title: 
status: 
depends_on: 
summary: 
openspec_change: 

```

I feel the above sections are self explantory but the ITEMS are where the real work gets done.

So in a Milestone we may have several items that need to be created, here's an example of the first roadmap item from a RAG pipeline app:

```text
## Items

id: RAG-M1-001
title: Scrape Sample Data Set
status: todo
depends_on: none
summary: Scrape a representative sample of the locally running company documentation found at http://localhost:8000 and persist it as JSONL in ./src/scraped_output
openspec_change: 
```

The id field consists of our app name shortened RAG, Milestone M1 and unique item number 001. This can really consist of anything you'd like but for consistency the aforementioned format is best to stick to, as your system will need to keep these IDs as reference throughout the development process. 

The status lets the agent know if the work is still to be done, has a change in place already that needs to be executed or if it is done, archived etc. This part is important and is mostly set as todo by you initially and then taken care of the agent subsequently.

The status are:
todo
proposed
done
archived

More statuses may be added in future but again this is for clarity with the agent whereas it is intended humans just create a todo item.

Depends on gives our system an understanding of what needs to have been done before this item can be done. For now it's our first item so has no prior work it is dependent on. In future the system will infer this, but as a starting point it is worth thinking of work order early on

The summary is quite important as the LLM will use this to create the work item, so keep it focused and specific. If you find yourself using the work and or this becomes much longer than a couple of sentencing think about breaking things up into different items. Focus is key these will directly map to the changes created for use with OpenSpec.

Once you have your first Roadmap item you are ready to use the /openroad command with OpenCode to run thing:

![Alt text](images/opencode_openroad_command.png)

You'll notice we have 2 openroad commands /openroad and /openroad-close. /openroad-close is used to archive and close the currently changed (done) items much like the /opsx-archive command it will close the OpenSpec change and make the necessary changes on our Roadmap to move onto the next item. It's important that you run these after you are happy with the changes made using the /openroad command.


### Future development plans?

1. Tighten up how existing files that the system uses are handled
2. Work with Product Requirements Documents (PRDs) as a way to produce intial Roadmaps (roadmap.md files)
3. Work on a dashboard coordination tool so that a user can have better overview of the roadmap state and units of work/changes

### Contributions?

Code contributions by other developers is currently closed, but what I am looking for is feedback and an understanding of YOUR particular workflow so we can make sure this tool has the best user experience out there!

## Where is this Going?

In future I hope OpenRoad will become a higher level Agent Coordination tool that can be the first touch point for working on projects.

The human should be kept in the loop, with the aim as Agents to act as peers you collobrate with on anything from small project to large business products
