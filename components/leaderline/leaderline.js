// import LeaderLine from '/node_modules/leader-line/leader-line.min.js';

const LeaderLine = window.LeaderLine;

export default {
  props: {
    startElement: String,
    endElement: String,
    color: String,
    size: Number,
    hide: Boolean
  },
  setup(props, { emit }) {
    let line = new LeaderLine(
      document.getElementById(props.startElement),
      document.getElementById(props.endElement),
      { color: props.color, size: props.size, hide: props.hide }
    );
    const handle_show = () => {
      line.show();
      emit('show');
    }
    const handle_hide = () => {
      line.hide();
      emit('hide');
    }
    return {
      handle_show,
      handle_hide
    }
  }
}
