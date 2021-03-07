-- 6a (execution: 17 s 53 ms, fetching: 63 ms)
select b.primaryTitle ,e.seasonNumber, e.episodeNumber, r.averageRating from `title.ratings` r
inner join `title.episode` e on r.tconst = e.tconst
inner join `title.basic` b on b.tconst = e.tconst
where r.tconst in
      (select tconst from `title.episode`
where parentTconst = 'tt0944947')
order by r.averageRating desc
limit 5