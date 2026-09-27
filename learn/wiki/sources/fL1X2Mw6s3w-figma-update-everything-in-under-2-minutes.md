---
type: source
title: "Figma Update: Everything In Under 2 Minutes"
created: 2026-09-27
updated: 2026-09-27
video_id: fL1X2Mw6s3w
url: https://www.youtube.com/watch?v=fL1X2Mw6s3w
channel: Kole Jain
published: 2024-03-13T22:09:02Z
authority: reference
tags:
  - figma
  - multi-edit
  - auto-layout
  - layer-naming
  - sections
  - design-tools
  - kole-jain
---

# Figma Update: Everything In Under 2 Minutes

## Metadata

- Video ID: `fL1X2Mw6s3w`
- Channel: Kole Jain
- Published: 2024-03-13T22:09:02Z
- URL: https://www.youtube.com/watch?v=fL1X2Mw6s3w

## Summary

Kole Jain runs through Figma's multi-edit update in about a minute. Multi-edit lets a designer select matching elements across many frames and change them all as if editing each one on its own, which he says used to be a real pain. Figma finds the matching layers by their naming scheme and the position of their groupings, and the same feature can change the text of several text objects at once. He also shows applying auto layout across several frames with Shift+A, moving an element in every auto layout at once, and using a section to limit a multi-edit to only some frames. For someone building a design system, it is a tooling tip for keeping repeated frames and screens in step inside Figma, and a hint that consistent layer naming pays off [inferred].

## Key Ideas

- Figma's multi-edit lets you select matching elements across frames and change them all as if editing each one independently.
- Before the update, making the same change to repeated elements was, in his words, a giant pain.
- Figma guesses which layers match by the layers' naming scheme and the position of their groupings.
- Multi-edit also works on text: several text objects can be changed at the same time.
- Auto layout can be applied across frames at once by selecting the elements and pressing Shift+A (captioned 'shift plus a').
- An element can be selected and moved in all of the auto layouts at the same time.
- A section limits a multi-edit to only the frames inside it.
- Consistent layer names and grouping across repeated frames make multi-edit's matching more useful [inferred].

## Entities

- [[entities/kole-jain|Kole Jain]] (person): Owner of the YouTube channel that published the video; a UI/UX designer [inferred].
- [[entities/figma|Figma]] (tool): The design tool whose multi-edit update the video covers.
- [[entities/multi-edit|Multi-edit]] (concept): Figma feature for selecting matching layers across frames and editing them together.
- [[entities/auto-layout|Auto layout]] (concept): Figma layout feature that can now be applied and adjusted across several frames at once.
- [[entities/section|Section]] (concept): Figma container used here to scope a multi-edit to only the frames inside it.

## Topics

- [[topics/figma-and-design-tools|Figma and design tools]]: Covers Figma's multi-edit update: selecting matching layers by name and grouping, editing several text objects together, applying and adjusting auto layout across frames with Shift+A, and scoping multi-edit with a section.

## Notable Claims

- Multi-edit lets you select and apply changes to each element as if you were editing them independently. Evidence: multi-edit gives you the ability to select and apply changes to each element
- Editing matching elements in Figma before the update was very painful (the presenter's opinion). Evidence: to be honest it was a giant pain
- Figma guesses which matching layers you want to edit by matching the naming schemes of the layers and the position of the groupings. Evidence: by matching the naming schemes of the layer and the position of the groupings
- Multi-edit can change the text of multiple text objects at the same time. Evidence: it can also edit multiple text objects
- Auto layout can be applied across frames by selecting the elements and pressing Shift+A. Evidence: selecting our elements and hitting shift plus a
- An element can be selected and moved for all of the auto layouts at the same time. Evidence: move it for all of the auto layouts at the same time
- Placing frames in a section scopes a multi-edit so only the frames within the section are edited. Evidence: scope a multi-edit to only a portion of the frames available using a section

## Quotes

> multi-edit gives you the ability to select and apply changes to each element
> figma can now guess which matching layers you want to edit

<!-- od:learn -->

## For OpenDesigner

- Authority: **reference**
- Caveat: Dated: it covers Figma's multi-edit update as of March 2024; controls and shortcuts may have changed since.
- Caveat: The narration refers to 'this button' without naming it, so the exact controls for selecting matches and editing text are only visible on screen, not in the transcript.
- Caveat: Auto-caption errors: 'shift plus a' is read as the Shift+A shortcut, and 'mult edited' as multi-edited.
- Caveat: The title says under 2 minutes; the video runs 1 minute 4 seconds and is a feature overview, not design guidance.
- Caveat: Calling the old behaviour 'a giant pain' is the presenter's opinion.

### Rules and practices

- **consider** (tooling, all): In Figma, use multi-edit to select all matching layers across frames and change them together, instead of editing each repeated element one by one. Why: Multi-edit applies the change to each element as if it were edited independently; the old way was, in his words, a giant pain. [multi-edit gives you the ability to select and apply changes to each element]
- **consider** (tooling, all): Keep layer names and grouping positions consistent across repeated frames so Figma's multi-edit can find the matching layers [inferred]. Why: Figma picks matching layers by the naming schemes of the layers and the position of the groupings. [by matching the naming schemes of the layer and the position of the groupings]
- **consider** (tooling, all): To add auto layout across several frames at once, select their elements and press Shift+A (the captions read 'shift plus a'). Why: Auto layout can now be applied across frames in one step. Values: shift plus a. [apply Auto layout across frames by selecting our elements and hitting shift plus a]
- **consider** (tooling, all): To limit a multi-edit to only some frames, put those frames inside a Figma section. Why: Only the frames within the section have their elements multi-edited. [scope a multi-edit to only a portion of the frames available using a section]
- **consider** (tooling, all): To change the text of several matching text objects at once, select them with multi-edit and edit the text once. Why: Multi-edit can edit multiple text objects and change the text for all elements at the same time. [change the text for all elements at the same time]
- **consider** (tooling, all): To reposition the same element in many auto layout frames, select it across them and move it once. Why: The element can be selected and moved for all of the auto layouts at the same time. [select an element and move it for all of the auto layouts at the same time]

### Process

1. Select matching layers: Select an element and press the multi-edit button; Figma grabs all matching layers, matched by layer naming scheme and grouping position.
2. Edit text together: Use the multi-edit controls on several text objects, then change the text for all of them at the same time.
3. Apply auto layout across frames: Select the elements in several frames and press Shift+A to add auto layout to all of them.
4. Move an element in every auto layout: Select an element and move it; the move is applied in all of the auto layouts at the same time.
5. Scope with a section: Place the frames you want to change inside a section so only the frames within it are multi-edited.

### Examples and visual references

- Before-and-after of editing matching elements across frames (Figma): The video contrasts how Figma behaved before the update, where matching elements had to be changed separately [inferred], with multi-edit changing them all at once (described from the narration; the on-screen visuals were not seen).
- Multi-edit scoped by a section (Figma): Frames are placed inside a section so a multi-edit changes only the elements in those frames and leaves the other frames alone (described from the narration; the on-screen visuals were not seen).

<!-- /od:learn -->
