from tensorforce.execution import Runner
import agent_conf, data

data.wipe_rows(agent_conf.AGENT_NAME)
conf = agent_conf.conf(
    tf_saver=False,
    tf_summary="logs_async",
    tf_summary_level=3,
)

runner = Runner(agent=conf['agent'], environment=conf['env'])
runner.run(episodes=agent_conf.EPISODES)