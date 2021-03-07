-- 6d (execution: 12 s 199 ms, fetching: 16 ms)
select b.primaryTitle ,e.seasonNumber, e.episodeNumber, r.numVotes from `title.ratings` r
inner join `title.episode` e on r.tconst = e.tconst
inner join `title.basic` b on b.tconst = e.tconst
where r.tconst in
      (select tconst from `title.episode`
where parentTconst = 'tt0944947')
order by r.numVotes asc
limit 5