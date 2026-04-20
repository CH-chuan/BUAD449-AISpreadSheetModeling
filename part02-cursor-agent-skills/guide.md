# Part 2 — Build a Cursor Skill

In Part 1, you used Cursor to help set up your environment. In this part, you'll use Cursor to build a **reusable skill**: a small set of instructions that teaches the agent how to handle a recurring task in a consistent way.

The key idea is that you do **not** start from a blank page. Cursor already has a built-in skill for this: **`create-skill`**. Your job is to use that skill to guide the process, then refine the result based on the behavior you want from the agent.

---

## What This Part Is About

This guide is about the **general workflow** for creating a skill, not about one specific domain.

For LP-specific examples, use the companion files:

- `part02-cursor-agent-skills/solver.md`
- `part02-cursor-agent-skills/formulator.md`

Those two files show how the same general process can produce two different skills:

- one for **solving** linear programs,
- one for **formulating** linear programs.

That separation matters because students should learn:

1. the **general method** for building a skill,
2. the **domain-specific choices** for a particular skill,
3. how to reproduce the process on a new task later.

---

## Step 1: Start with `create-skill`

Instead of manually designing the skill structure yourself, ask Cursor to use the **`create-skill`** skill.

Here is the kind of prompt to give:

> `/create-skill I want to build a project skill for [task]. Let's first discuss scope, trigger conditions, and the output format.`

This is the key move. The `create-skill` skill gives you a framework for:

- defining the purpose of the skill,
- deciding what belongs in scope,
- deciding where the skill should live,
- deciding what output format should be controlled,
- and creating the actual files.

So the first lesson is:

> **Use a skill to build a skill.**

---

## Step 2: Gather Requirements Through Discussion

Once `create-skill` is active, the next step is **discussion**, not immediate writing.

Before writing files, clarify questions like:

1. What repeated task should the skill handle?
2. What is **in scope** and **out of scope**?
3. When should the agent automatically use the skill?
4. What output format must stay consistent?
5. What details belong in the main file versus support files?

This is the stage where the skill becomes useful rather than generic.

One of the most important design lessons is:

> For many skills, the internal reasoning can stay flexible, but the **scope** and **output format** should be explicit.

---

## Step 3: Turn Requirements Into Skill Files

After the requirements are clear enough, Cursor can write the skill files directly.

For most project skills, the files live under:

- `.cursor/skills/<skill-name>/`

The most common structure is:

### `SKILL.md`

This is the main file and the **entry point** for the skill. It tells the agent:

- when to use the skill,
- what problems are in scope,
- what workflow to follow,
- and what output structure to produce.

`SKILL.md` should contain the essential instructions needed for the agent to start the task correctly without having to read every support file first.

### `reference.md`

This file holds supporting details that are useful but would make `SKILL.md` too long or too cluttered.

Typical content includes:

- definitions,
- implementation notes,
- formulas or patterns,
- tool-specific details,
- or interpretation guidance.

The agent should read `reference.md` only when `SKILL.md` points to it and the current task needs that extra detail.

### `examples.md` (optional)

Use this when students or future agents will benefit from one or more worked examples.

This is especially helpful when:

- the workflow is conceptually simple but easy to misapply,
- there is a standard answer style,
- or you want the skill to be more reproducible for beginners.

The agent should read `examples.md` only when `SKILL.md` points to it and a worked example would improve correctness, consistency, or teaching value.

### `scripts/` (optional)

Use this when the skill depends on repeatable operations that are fragile, tedious, or better handled by a prepared utility than by generating code from scratch each time.

Common uses include:

- validation helpers,
- file analyzers,
- repeatable transformations,
- or domain-specific utilities that should behave consistently.

The agent should use scripts only when `SKILL.md` explicitly says to **run** them or **read** them.

The lesson here is:

> Keep `SKILL.md` focused. Put secondary detail in support files.

Another important rule is:

> Start with `SKILL.md`. Read support files only by need.

In practice, that means:

- use `reference.md` for extra detail,
- use `examples.md` for worked patterns,
- use `scripts/` for explicit executable helpers.

This is sometimes called **progressive disclosure**: keep the main instructions short, and only pull in more detail when the current task actually needs it.

### When To Add Each Support File

Add `reference.md` when:

- the skill needs formulas, patterns, implementation notes, or interpretation rules,
- but those details are not required for every single use.

Add `examples.md` when:

- students need a worked example to reproduce the workflow,
- the answer style needs to stay consistent,
- or the task is easy to misunderstand without a concrete model.

Add `scripts/` when:

- a repeated operation is fragile or hard to reproduce from plain instructions,
- validation should be run the same way every time,
- or a prepared tool is more reliable than generating fresh code in each session.

Do **not** add support files automatically. Add them only when they make the skill more reliable, more teachable, or more reproducible.

---

## Step 4: Refine the Skill Through Iteration

The first draft is usually not the final draft.

Skill creation is usually a short cycle of:

1. draft,
2. review,
3. sharpen scope,
4. remove low-value detail,
5. add the missing outputs that matter.

Good skills usually improve by becoming:

- narrower,
- clearer,
- easier to trigger correctly,
- and more consistent in output.

Another lesson:

> Good skills get better by becoming **narrower, clearer, and more useful**.

---

## Step 5: Verify the Skill on a Real Task

Do not stop after writing the files. Test the skill on a real example.

Testing helps you catch problems such as:

- the skill being too broad,
- the agent missing an expected section,
- the output being technically correct but not useful,
- or the support files being in the wrong place.

For reproducibility, use a real task that looks like what students will actually do.

That way you can check not only whether the skill works, but whether it produces results in the style you want students to learn from.

---

## Step 6: Save, Commit, and Reuse

Once the skill behaves the way you want, keep it in the project so it can be reused.

For project skills, the usual location is:

- `.cursor/skills/<skill-name>/`

This is what makes skills powerful: once the instructions are encoded well, you no longer need to restate the same expectations every time.

It also improves reproducibility for students because the workflow is saved in the repository rather than living only in a chat transcript.

---

## What You Just Did

You used Cursor in a more advanced way:

- not just to solve a problem,
- but to **teach the agent how to solve a class of problems**.

That is the main idea behind agent skills.

You also learned a practical workflow for building them:

1. start with **`create-skill`**,
2. discuss the requirements,
3. write `SKILL.md` and any support files,
4. refine through iteration,
5. test on a real example,
6. commit the result for reuse.

---

## Quick Checklist for Building Your Own Skill

Before asking Cursor to create a skill, make sure you can answer these questions:

1. What repeated task do I want the agent to handle?
2. What is **in scope** and **out of scope**?
3. What output format must stay consistent?
4. What details belong in `SKILL.md`?
5. What details should be moved to `reference.md` or `examples.md`?
6. How will I test the skill on a real example?

If you can answer those, then `create-skill` can usually help you build the rest.

---

## Suggested Prompt Pattern

When you want to create a new skill, start with something like:

> `/create-skill I want to build a project skill for [task]. Let's first discuss scope, trigger conditions, and the exact output format I want.`

That prompt works because it tells Cursor to do two things:

- use the **skill-creation framework**,
- and start with **discussion before implementation**.

That is usually the best way to build a high-quality skill.

---

## Companion Examples

Use these files after reading this guide:

- `part02-cursor-agent-skills/solver.md` for a solver-specific worked example
- `part02-cursor-agent-skills/formulator.md` for a formulation-specific worked example

Together, they show how one general process can be adapted into multiple skills with different scopes.
