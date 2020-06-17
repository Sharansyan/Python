#
# Programming Assignment-1: Computing Paradox

**Due on 2020-03-12, 23:59 IST**

You are provided with a playlist containing  **N**  songs, each has a unique positive integer length. Assume you like all the songs from this playlist, but there is a song, which you like more than others.
 It is named &quot;Computing Paradox&quot;.

 You decided to sort this playlist in increasing order of songs length. For example, if the lengths of the songs in the playlist were {1, 3, 5, 2, 4} after sorting it becomes {1, 2, 3, 4, 5}.
 Before the sorting, &quot;Computing Paradox&quot; was on the  **k**** th** position (1-indexing is assumed for the playlist) in the playlist.

 Your task is to find the position of &quot;Computing Paradox&quot; in the sorted playlist.

**Input Format:**
 The first line contains two numbers  **N**  denoting the number of songs in the playlist.
 The second line contains  **N**  space separated integers  **A**** 1 ****, A**** 2 ****, A**** 3 ****,..., A**** N** denoting the lengths of songs.
 The third line contains an integer  **k** , denoting the position of &quot;Computing Paradox&quot; in the initial playlist.

**Output Format:**

 Output a single line containing the position of &quot;Computing Paradox&quot; in the sorted playlist.

**Example:**

**Input:**
 4
 1 3 4 2
 2


**Output:**

3

**Explaination:**

N equals to 4, k equals to 2, A equals to {1, 3, 4, 2}. The answer is 3 because {1, 3, 4, 2} -\&gt; {1, 2, 3, 4}.
